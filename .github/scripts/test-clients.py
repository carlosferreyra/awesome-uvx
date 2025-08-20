# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import json
import subprocess
import sys
from collections.abc import Iterable
from pathlib import Path

# get a list of all packages in the list

uv_download = "curl -LsSf https://astral.sh/uv/install.sh | sh"


def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()


def run_command_safe(command):
    """Run a shell command and return (success, output, error)."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.returncode == 0, result.stdout.strip(), result.stderr.strip()


def main():
    """Main function to run the UVX test clients."""
    print("Script started successfully!")
    print("Running UVX test clients...")

    # Install UV if not already installed
    try:
        uv_version = run_command("uv --version")
        print(f"UV version: {uv_version}")
    except SystemExit:
        print("UV not found, installing...")
        run_command(uv_download)
        print("UV installed successfully!")

    # Run the UVX test clients
    command_list: list[Iterable] = []
    json_folder = Path(__file__).parent / "placeholders"
    print(f"Looking for JSON files in: {json_folder}")

    for json_file in json_folder.glob("*.json"):
        print(f"Processing file: {json_file.name}\n")
        with open(json_file, "r") as f:
            data = json.load(f)
            print(f"Top-level keys in {json_file.name}:\n {list(data.keys())}")

            # The structure is: {"category-name": {"package-name": {"execs": [...]}}}
            for _, packages in data.items():
                # Skip if the category doesn't contain a dictionary of packages
                if not isinstance(packages, dict):
                    continue

                for package_name, package_info in packages.items():
                    match package_info:
                        # Case 1: Matches a dict with a key "execs"
                        # that holds a list with at least one item.
                        # It captures the first item as 'first_exec'.
                        case {"execs": [first_exec, *_]}:
                            print(
                                f"Found executable '{first_exec}' for package '{package_name}'"
                            )
                            command_list.append((first_exec, package_name))

                        # Case 2: Matches if the "execs" list is empty.
                        case {"execs": []}:
                            print(f"No executables found for package '{package_name}'")

                        # Case 3 (Default): Catches any other structure.
                        case _:
                            print(f"Invalid package structure for '{package_name}'")

    print(f"Total executables found: {len(command_list)}")

    # Initialize counters
    success_count = 0
    failed_packages = []

    # Open output log file for writing (only for failures)
    output_log_path = Path("./output.log")
    with open(output_log_path, "w") as log_file:
        log_file.write("UVX Test Clients - Failed Executions Log\n")
        log_file.write("=" * 50 + "\n\n")

        for exec_name, package_name in command_list:
            print(f"Testing: {package_name} ({exec_name})")

            # Test method 1: uv tool install package-name
            command1 = f"uv tool install --force {package_name}"
            success1, output1, error1 = run_command_safe(command1)

            # Test method 2: uvx --from package-name cli-entrypoint -h
            command2 = f"uvx --from {package_name} {exec_name} -h"
            success2, output2, error2 = run_command_safe(command2)

            if success1 or success2:
                success_count += 1
                method = "uv tool install" if success1 else "uvx --from"
                print(f"  ✓ Success with: {method}")
            else:
                # Both methods failed - log to file
                failed_packages.append(package_name)
                print("  ✗ Failed: both methods")

                log_file.write(f"Package: {package_name}\n")
                log_file.write(f"Executable: {exec_name}\n")
                log_file.write("Status: FAILED\n\n")

                log_file.write(f"Method 1 - Command: {command1}\n")
                log_file.write(f"Method 1 - Success: {success1}\n")
                log_file.write(f"Method 1 - Output: {output1}\n")
                log_file.write(f"Method 1 - Error: {error1}\n\n")

                log_file.write(f"Method 2 - Command: {command2}\n")
                log_file.write(f"Method 2 - Success: {success2}\n")
                log_file.write(f"Method 2 - Output: {output2}\n")
                log_file.write(f"Method 2 - Error: {error2}\n")

                log_file.write("-" * 50 + "\n\n")

    print("\nExecution Summary:")
    print(f"  Total packages tested: {len(command_list)}")
    print(f"  Successful: {success_count}")
    print(f"  Failed: {len(failed_packages)}")

    if failed_packages:
        print(f"  Failed packages logged to: {output_log_path.absolute()}")
    else:
        print("  All packages succeeded! No log file created.")
        # Remove empty log file if no failures
        if output_log_path.exists():
            output_log_path.unlink()


if __name__ == "__main__":
    main()
