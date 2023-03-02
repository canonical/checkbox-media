#!/usr/bin/python3
#
# Measures the energy used (in μjoules) while a command was running.
# NOTE: This includes energy for all processes, not just the command.
#       So run this on an otherwise idle machine.
#
# What zones are reported depends on the RAPL zones supported by the 
# hardware.
#
# By Bram Stolk (bram.stolk@canonical.com)

import os
import sys
import subprocess
import time

dirnames = {}

def find_zones():
        cmd = "find /sys/devices/virtual/powercap/intel-rapl -name intel-rapl\:\* -print";
        f = os.popen(cmd, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
                line = line.strip()
                nm = line + "/name"
                f = open(nm, "r")
                assert(f)
                name = f.readline().strip()
                f.close()
                dirnames[name] = line
        return len(dirnames.keys())


def measure():
        energy = {}
        measure_time = time.time()
        for k in dirnames.keys() :
                nm = dirnames[k] + "/energy_uj"
                f = open(nm, "r")
                line = f.readline().strip()
                uj = int(line)
                f.close()
                energy[k] = uj
        return measure_time, energy

def report(energy0_stat, energy1_stat) :
        energy0 = energy0_stat[1]
        energy1 = energy1_stat[1]
        print("Performance counter stats for 'system wide':")
        for k in dirnames.keys() :
                e0 = energy0[k]
                e1 = energy1[k]
                assert(e1 >= e0)
                print("\t%.6f Joules power/energy-%s/" % ((e1-e0)/1000000, k))

        elapsed_time = energy1_stat[0] - energy0_stat[0]
        print("\t%.6f seconds time elapsed " % elapsed_time)

if __name__ == '__main__' :
        if len(sys.argv) < 2 :
                print("Usage:", sys.argv[0], "command")
                sys.exit(1)

        timeout = int(sys.argv[1])

        num = find_zones()
        if num == 0 :
                print("No RAPL zones were found. Aborting.")
                sys.exit(2)

        # run the commands
        user = os.environ.get("SUDO_USER")
        assert(user)

        start_time, energy0 = measure()
        time.sleep(timeout)
        end_time, energy1 = measure()

        report((start_time, energy0), (end_time, energy1))
