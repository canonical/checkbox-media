#!/usr/bin/env python3

import re
import sys
import statistics

p_float='\d+\.\d+'
energy_str = f'({p_float}) Joules power/energy-([a-z0-9\-_]+)/'
time_str = f'({p_float}) seconds time elapsed'

energy_pattern = re.compile(energy_str)
time_pattern = re.compile(time_str)

def load_energy(fname: str ) -> tuple[float, dict[str, float]]:
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

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    hwacc_energy_file = sys.argv[1]
    no_hwacc_energy_file = sys.argv[2]
    min_gain = float(sys.argv[3])

    hwacc_energy = load_energy(hwacc_energy_file)
    no_hwacc_energy = load_energy(no_hwacc_energy_file)
    
    print(f'Enabled: {hwacc_energy}')
    print(f'Disabled: {no_hwacc_energy}')

    gain_energy = {}    
    for key, value in hwacc_energy[1].items():
        hwacc_joule_per_sec = value / hwacc_energy[0]
        no_hwacc_joule_per_sec = no_hwacc_energy[1][key] / no_hwacc_energy[0]
        if no_hwacc_joule_per_sec != 0:
            gain = ((no_hwacc_joule_per_sec - hwacc_joule_per_sec) / no_hwacc_joule_per_sec) * 100
        else:
            gain = -1000000 * hwacc_joule_per_sec
        gain_energy[key] = gain

    avg_gain = statistics.mean(gain_energy.values())

    print((avg_gain, gain_energy))

    if avg_gain < min_gain:
        sys.exit(1)

sys.exit(0)

