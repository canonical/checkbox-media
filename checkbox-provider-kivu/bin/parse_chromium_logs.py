#!/usr/bin/env python3

import argparse
import os.path
import sys

HW_DECODERS = ["VDAVideoDecoder", "VaapiVideoDecoder"]
SW_DECODERS = ["FFmpegVideoDecoder", "Dav1dVideoDecoder"]


def parse(log_file):
    """
    Parse Chromium log file to retrieve Video Decoder being used.
    """
    if not os.path.isfile(log_file):
        raise FileNotFoundError("{} not found.".format(log_file))

    with open(log_file) as f:
        log = f.readlines()

    found_decoders = []

    for line in log:
        for decoder in HW_DECODERS + SW_DECODERS:
            if decoder in line:
                found_decoders.append(decoder)

    if not found_decoders:
        return None

    # Grabbing last found decoder as Chromium spits a list of available
    # decoders before using one
    decoder = found_decoders[-1]
    return decoder


def is_hw_decoder(decoder):
    if decoder in HW_DECODERS:
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse Chromium log file to look for used Video Decoder."
    )
    parser.add_argument(
        "logfile", help="Path to the Chromium log file to parse."
    )
    args = parser.parse_args()
    decoder = parse(args.logfile)
    if decoder:
        if is_hw_decoder(decoder):
            print("Chromium is using hardware decoder ({})".format(decoder))
        else:
            sys.exit(
                (
                    "Error: Chromium does not seem to be using a hardware "
                    "decoder (found decoder: {})".format(decoder)
                )
            )
    else:
        sys.exit(
            (
                "Error: No decoder found in the log. "
                "Check that the proper version of Chromium is being used."
            )
        )
