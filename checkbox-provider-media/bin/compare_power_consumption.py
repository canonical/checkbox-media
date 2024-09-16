#!/usr/bin/env python3

import re
import sys
import statistics

p_float='\d+\.\d+'
energy_str = f'({p_float}) Joules power/energy-([a-z0-9\-_]+)/'
time_str = f'({p_float}) seconds time elapsed'

energy_pattern = re.compile(energy_str)
time_pattern = re.compile(time_str)

def load_energy(fname: str) -> tuple[float, dict[str, float]]:
    """
    Load file output by rapl-power-stat.py
    The return value is a 2-tuple of time (sec) and dict
      The dict:
        - key : power zone name
        - value ; joules values
      Example: (600.097183, {'psys': 9976.218114, 'package-0': 3658.829745, 'core': 825.515099, 'uncore': 318.009806})
    """
    energy_usage = {}
    duration = 0.0
    with open(fname, 'r') as f:
        for line in f.readlines():
            result = time_pattern.match(line.strip())
            if result is not None:
                duration = float(result.group(1))
            result = energy_pattern.match(line.strip())
            if result is None:
                continue
            energy_usage[result.group(2)] = float(result.group(1))

    return (duration, energy_usage)

def get_energy_usage(rapl_output):
    """
    Return total energy usage according to a RAPL output
    """
    consumed_energy = rapl_output.get('package-0', 0.0)
    # on some recent architectures, we have psys package that includes package-0
    consumed_energy = max(consumed_energy, rapl_output.get('psys', 0.0))
    return consumed_energy

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    hwacc_energy_file = sys.argv[1]
    no_hwacc_energy_file = sys.argv[2]
    min_gain = float(sys.argv[3])

    hwacc_energy = load_energy(hwacc_energy_file)
    no_hwacc_energy = load_energy(no_hwacc_energy_file)

    hwacc_cons = get_energy_usage(hwacc_energy[1])
    no_hwacc_cons = get_energy_usage(no_hwacc_energy[1])

    print(f'Enabled: {hwacc_energy} - Consumption : {hwacc_cons}')
    print(f'Disabled: {no_hwacc_energy} - Consumption : {no_hwacc_cons}')

    hwacc_duration_sec = hwacc_energy[0]
    no_hwacc_duration_sec = no_hwacc_energy[0]
    if (hwacc_duration_sec <= 0) or (no_hwacc_duration_sec <= 0):
        sys.exit(1)

    hwacc_joule_per_sec = hwacc_cons / hwacc_duration_sec
    no_hwacc_joule_per_sec = no_hwacc_cons / no_hwacc_duration_sec

    if no_hwacc_joule_per_sec <= 0:
        sys.exit(1)

    gain = ((no_hwacc_joule_per_sec - hwacc_joule_per_sec) / no_hwacc_joule_per_sec) * 100

    print(f'Gain : {gain}%')

    if gain < min_gain:
        sys.exit(1)

sys.exit(0)

