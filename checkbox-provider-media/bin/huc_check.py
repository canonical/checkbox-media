#!/usr/bin/python3

import subprocess
import sys

def is_huc_running():
    try:
        result = subprocess.run(["sudo", "find", "/sys/kernel/", "-name", "huc_info"], capture_output=True, text=True, check=True)
        filename = result.stdout.strip()
        with open(filename, 'r') as f:
            output = f.readlines()
            # huc_info is multi-line. Loop through to find status
            for line in output:
                if "status: RUNNING" in line:
                    return True
        # HuC is not running if "status: RUNNING" is not in any output line
        return False
    except subprocess.CalledProcessError as e:
        print("Error finding HuC's status:", e)
        print("Stderr:", e.stderr)
        exit(1)

if __name__ == "__main__":
    if is_huc_running():
        print("HuC is running")
        exit(0)
    else:
        print("HuC is not running", file=sys.stderr)
        exit(1)
