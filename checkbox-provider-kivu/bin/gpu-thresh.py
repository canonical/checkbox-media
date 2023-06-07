#!/usr/bin/env python3
#
# GPU load measure tool on top of
# - intel_gpu_top for Intel
# - AMD Radeon currently unsupported
#
# This tool expects as input:
# - graphic card type (i915 or amdgpu)
# - measure duration
#
# The tool will output the amount of time spent above the specified video engine threshold to stdout.
#
# By Shane McKee (shane.mckee@canonical.com)

import os
import argparse
import subprocess
from gpu_utils import compute_time_above_thresh_intel, get_num_active_engines

def load_intel(fname : str, timeout : int) -> float:
    try:
        os.remove(fname)
    except OSError:
        pass

    try:
        # intel_gpu_top requires root privileges
        if os.geteuid() != 0:
            print('intel_gpu_top requires root privileges !')
            return None
        subprocess.check_call(f'timeout {timeout} intel_gpu_top -J > {fname}', stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL, shell=True)
    except subprocess.CalledProcessError as e:
        if e.returncode == 124:
            pass
        else:
            print(f'Error running intel_gpu_top : {e.returncode}')
            return None

    return compute_time_above_thresh_intel(fname, threshold)

if __name__ == "__main__":
    script = os.path.basename(__file__)
    parser = argparse.ArgumentParser(
        description=("Compute time spent above the specified video engine threshold")
    )
    parser.add_argument(
        "--timeout", type=int, help="Measure duration in seconds"
    )
    parser.add_argument(
        "--gpu", type=str, help="GPU driver (amdgpu, i915)"
    )
    parser.add_argument(
        "--file", type=str, help="Stat output file"
    )
    parser.add_argument(
        "--threshold", type=float, help="Minimum threshold for video engine utilization"
    )
    args = parser.parse_args()

    timeout = 1 if args.timeout is None else args.timeout
    gpu_driver = 'i915' if args.gpu is None else args.gpu
    fname = '/tmp/gpu-thresh-5ef38178-c2c0-11ed-afa1-0242ac120002.data' if args.file is None else args.file
    threshold = 0 if args.threshold is None else args.threshold

    if gpu_driver == 'amdgpu':
        # This script does not support amd yet
        print(-1)
    if gpu_driver == 'i915':
        time_above_threshold = load_intel(fname=fname, timeout=timeout)

    # Divide that time by the number of active video engines
    time_above_threshold = time_above_threshold/get_num_active_engines(fname=fname)

    print(time_above_threshold)
