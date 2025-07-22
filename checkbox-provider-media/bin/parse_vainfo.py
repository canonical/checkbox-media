#!/usr/bin/python3

import subprocess
import re

def get_codec_profiles():
    # List of codecs to check
    codec_profiles = {
        "AVC": ["VAProfileH264Main", "VAProfileH264High"],
        "MPEG-2": ["VAProfileMPEG2Simple", "VAProfileMPEG2Main"],
        "VC-1": ["VAProfileVC1Simple", "VAProfileVC1Main", "VAProfileVC1Advanced"],
        "JPEG": ["VAProfileJPEGBaseline"],
        "VP8": ["VAProfileVP8Version0_3"],
        "HEVC 8bit": ["VAProfileHEVCMain"],
        "HEVC 8bit 422" : ["VAProfileHEVCMain"],
        "HEVC 8bit 444" : ["VAProfileHEVCSccMain444"],
        "HEVC 10bit" : ["VAProfileHEVCMain10"],
        "HEVC 10bit 422" : ["VAProfileHEVCMain10"],
        "HEVC 10bit 444" : ["VAProfileHEVCMain444_10"],
        "HEVC 12bit" : ["VAProfileHEVCMain12"],
        "HEVC 12bit 422" : ["VAProfileHEVCMain422_12"],
        "HEVC 12bit 444" : ["VAProfileHEVCMain444_12"],
        "VP9 8bit": ["VAProfileVP9Profile0", "VAProfileVP9Profile1", "VAProfileVP9Profile2", "VAProfileVP9Profile3"],
        "AV1 8bit": ["VAProfileAV1Profile0"]
    }

    return codec_profiles

# Initialize the result dictionary
def init_codec_support_dict():
    codec_profiles = get_codec_profiles()
    return { codec: {"encode": False, "decode": False} for codec in codec_profiles }

def run_vainfo():
    # Run vainfo command and get output
    try:
        result = subprocess.run(["sudo", "vainfo"], capture_output=True, text=True, check=True)
        output = result.stdout + result.stderr  # vainfo sometimes prints to stderr
        return output
    except subprocess.CalledProcessError as e:
        print("Error running vainfo:", e)
        print("Stderr:", e.stderr)
        exit(1)

def get_codec_support_dict():
    # Regex pattern to find decode/encode support
    pattern = re.compile(r"(VAProfile[\w_]+).*VAEntrypoint(\w+)")
    codec_support = init_codec_support_dict()
    vainfo_output = run_vainfo()
    codec_profiles = get_codec_profiles()

    for line in vainfo_output.splitlines():
        match = pattern.search(line)
        if match:
            profile = match.group(1).upper()
            entrypoint = match.group(2).lower()
            # Match against codec aliases
            for codec, aliases in codec_profiles.items():
                if any(alias.upper() in profile for alias in aliases):
                    if "enc" in entrypoint:
                        codec_support[codec]["encode"] = True
                    elif "vld" in entrypoint:
                        codec_support[codec]["decode"] = True
    return codec_support

if __name__ == "__main__":
    supp_dict = get_codec_support_dict(...)
    print(supp_dict)
