
import sys
import os

# Ensure we are in the correct directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    from wake.cli.__main__ import main
except ImportError:
    print("Error: Could not import wake.cli.__main__. Ensure eth-wake is installed.")
    sys.exit(1)

if __name__ == "__main__":
    # Simulate command line arguments
    # We want to run: wake test tests/fuzz_wake.py
    sys.argv = ["wake", "test", "tests/fuzz_wake.py"]
    print(f"Running Wake validation with args: {sys.argv}")
    try:
        main()
    except SystemExit as e:
        print(f"Wake exited with code: {e.code}")
        sys.exit(e.code)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
