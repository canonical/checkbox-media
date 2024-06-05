#!/usr/bin/python3

import sys
import subprocess
import re

def support(va_output: str, codec : str, feature_type: str):
    codecs = set()
    for line in va_output.splitlines():
        if (codec in line) and (feature_type in line):
            codecs.add(codec)
    for codec in codecs:
        lc_codec = codec.lower()
        print(f'{feature_type}: {lc_codec}')
        print('')

def main():
    result = subprocess.run(['vainfo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    va_output = result.stdout.decode('utf-8')
    for codec in ['H264', 'VP8', 'VP9']:
        support(va_output, codec, 'VLD')
        support(va_output, codec, 'Enc')

if __name__ == "__main__":
    sys.exit(main())
