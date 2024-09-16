#!/usr/bin/env python3
#
# GPU load measure tool on top of
# - intel_gpu_top for Intel
# - radeontop for AMD Radeon
#
# This tool expects as input:
# - graphic card type (i915)
# - measure duration
#
# The tool will output the GPU current load in stdout.
#
# By Shane McKee (shane.mckee@canonical.com)

import os
import argparse
import subprocess
import json
import re
from gpu_utils import get_instant_video_engine_level



def load_intel(fname : str, timeout : float) -> int:
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

    return get_instant_video_engine_level(fname)

if __name__ == "__main__":
    script = os.path.basename(__file__)
    parser = argparse.ArgumentParser(
        description=("Compute current gpu load")
    )
    parser.add_argument(
        "--gpu", type=str, help="GPU driver (i915)"
    )
    parser.add_argument(
        "--file", type=str, help="Stat output file"
    )
    parser.add_argument(
        "--timeout", type=float, help="Measure duration in seconds"
    )
    args = parser.parse_args()

    timeout = 0.2 if args.timeout is None else args.timeout
    gpu_driver = 'i915' if args.gpu is None else args.gpu
    fname = '/tmp/gpu-load-instant-5ef38178-c2c0-11ed-afa1-0242ac120002.data' if args.file is None else args.file

    if gpu_driver == 'amdgpu':
        print("Error: AMD GPUs not supported yet.")
        exit(1)
    if gpu_driver == 'i915':
        gpu_load = load_intel(fname=fname, timeout=timeout)

    print(gpu_load)
