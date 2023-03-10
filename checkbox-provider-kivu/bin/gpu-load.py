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

def compute_avg_intel(fname : str) -> float:
    gpu_average = None
    with open(fname, 'r') as f:
        content = f.read().strip()

        # intel_gpu_top -J does not return valid JSON. The brackets are missing.
        if content[0] != "[":
            data = json.loads("[" + content + "]")
        else:
            data = json.loads(content)

        gpu_average = 0.0
        sumdata = {}
        for d in data:
            # Looking at the `engines` section only
            for k, v in d["engines"].items():
                # Focus on GPU usage for video encoding/decoding only
                if "Video/" in k and (v.get("busy") is not None):
                    if sumdata.get(k):
                        sumdata[k] += v["busy"]
                    else:
                        sumdata[k] = v["busy"]

        if data and sumdata:
            gpu_average = sum(sumdata.values()) / len(data)

    return gpu_average

def load_intel(fname : str, timeout : int) -> float:
    try:
        os.remove(fname)
    except OSError:
        pass

    try:
        subprocess.check_call(f'timeout {timeout} intel_gpu_top -J > {fname}', stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL, shell=True)
    except subprocess.CalledProcessError as e:
        if e.returncode == 124:
            pass
        else:
            print(f'Error running intel_gpu_top : {e.returncode}')
            return None

    return compute_avg_intel(fname)

# 1678281421.757137: bus 03, gpu 36.67%, ee 0.00%, vgt 0.83%, ta 32.50%, sx 32.50%, sh 0.83%, spi 36.67%, sc 36.67%, pa 0.00%, db 36.67%, cb 33.33%, vram 49.66% 973.19mb, gtt 1.34% 93.38mb, mclk 78.96% 0.947ghz, sclk 14.29% 0.200ghz
def load_radeon(fname : str, timeout : int) -> float:
    try:
        os.remove(fname)
    except OSError:
        pass
    subprocess.check_call(f'radeontop -d {fname} --dump-interval=1 --limit={timeout}', stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL, shell=True)
    # compute average
    with open(fname, 'r') as load_file:
        loads = []
        for line in load_file:
            # cur_load = [(timestamp, load)]
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
    fname = 'gpu-load.data' if args.file is None else args.file

    if gpu_driver == 'amdgpu':
        gpu_average = load_radeon(fname=fname, timeout=timeout)
    if gpu_driver == 'i915':
        gpu_average = load_intel(fname=fname, timeout=timeout)

    print(gpu_average)
