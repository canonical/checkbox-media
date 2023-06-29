#!/usr/bin/env python3
#
# GPU load measure tool on top of
# - intel_gpu_top for Intel
# - radeontop for AMD Radeon
#
# This tool expects as input:
# - graphic card type (i915 or amdgpu)
# - measure duration
#
# The tool will output the GPU average load in stdout.
#
# By Hector Cao (hector.cao@canonical.com)

import os
import argparse
import subprocess
import json
import re
import time
from gpu_utils import compute_avg_intel



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

    return compute_avg_intel(fname)

def get_amd_vcn():
    """
    Open /sys/kernel/debug/dri/0/amdgpu_pm_info
    and check for VCN (Video Core Next) activity
    Return:
      - -1 : if VCN is not present or error
      -  0 : if VCN is disabled
      - 100: if VCN is used
    """
    load = -1
    try:
        with open('/sys/kernel/debug/dri/0/amdgpu_pm_info', 'r') as f:
            file_content = f.read()
            if 'VCN: Enabled' in file_content:
                load = 100
            elif 'VCN: Disabled' in file_content:
                load = 0
            else:
                load = -1
    except OSError:
        print('Error reading /sys/kernel/debug/dri/0/amdgpu_pm_info')
        pass
    return load

def load_amd_vcn(timeout: int):
    total = 0
    remaining_time = timeout
    while True:
        total = total + get_amd_vcn()
        remaining_time = remaining_time - 1
        if remaining_time <= 0:
            return (total / timeout)
        time.sleep(1)

def load_amd(fname : str, timeout : int) -> float:
    # if VCN is available, use VCN
    if get_amd_vcn() != -1:
        return load_amd_vcn(timeout)
    return load_amd_radeontop(fname, timeout)

# 1678281421.757137: bus 03, gpu 36.67%, ee 0.00%, vgt 0.83%, ta 32.50%, sx 32.50%, sh 0.83%, spi 36.67%, sc 36.67%, pa 0.00%, db 36.67%, cb 33.33%, vram 49.66% 973.19mb, gtt 1.34% 93.38mb, mclk 78.96% 0.947ghz, sclk 14.29% 0.200ghz
def load_amd_radeontop(fname : str, timeout : int) -> float:
    try:
        os.remove(fname)
    except OSError:
        pass
    subprocess.check_call(f'radeontop -d {fname} --dump-interval=1 --limit={timeout}', stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL, shell=True)
    # compute average
    with open(fname, 'r') as load_file:
        loads = []
        for line in load_file:
            cur_load = re.findall(r"(\d+\.\d+):.+ gpu (\d+\.\d+)%", line.strip())
            assert(len(cur_load) == 1)
            loads = loads + cur_load
        gpu_average = sum(float(n) for _, n in loads) / len(loads)

        return gpu_average

if __name__ == "__main__":
    script = os.path.basename(__file__)
    parser = argparse.ArgumentParser(
        description=("Compute gpu load")
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
    args = parser.parse_args()

    timeout = 1 if args.timeout is None else args.timeout
    gpu_driver = 'i915' if args.gpu is None else args.gpu
    fname = '/tmp/gpu-load-5ef38178-c2c0-11ed-afa1-0242ac120002.data' if args.file is None else args.file

    if gpu_driver == 'amdgpu':
        gpu_average = load_amd(fname=fname, timeout=timeout)
    if gpu_driver == 'i915':
        gpu_average = load_intel(fname=fname, timeout=timeout)

    print(gpu_average)
