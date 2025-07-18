import platform
import subprocess
import re

def get_cpu_model():
    system = platform.system()
    try:
        output = subprocess.check_output(["lscpu"], text=True)
        for line in output.splitlines():
            if "Model name" in line:
                return line.split(":", 1)[1].strip()
    except Exception as e:
        print(f"Error retrieving CPU model: {e}")
        return None

# TODO: Identify Battlemage (BMG), Alchemist (DG2), Arctic Sound M (ATSM), DG1, and SG1 graphics cards
def identify_generation():
    cpu_name = get_cpu_model()
    if not cpu_name:
        return "Unknown"

    # Map generation number (5th, 6th, ..., 18th) to architecture codes
    generation_map = {
        5:  "BDW",  # Broadwell
        6:  "SKL",  # Skylake
        7:  "KBL",  # Kaby Lake
        8:  "CFL",  # Coffee Lake
        9:  "CML",  # Comet Lake
        10: "ICL",  # Ice Lake
        11: "TGL",  # Tiger Lake
        12: "ADL",  # Alder Lake
        13: "RPL",  # Raptor Lake
        14: "MTL",  # Meteor Lake
        15: "ARL",  # Arrow Lake
        16: "LNL",  # Lunar Lake
        18: "PTL",  # Panther Lake
    }

    # Try to extract generation number from model name
    match = re.search(r"i[3579]-?(\d{4,5})", cpu_name)
    if match:
        model_num = match.group(1)
        if len(model_num) == 4:
            gen = int(model_num[0])
        elif len(model_num) == 5:
            gen = int(model_num[:2])
        else:
            return "Unknown"

        return generation_map.get(gen, "Unknown")

    return "Unknown"

def get_media_driver_category():
    gen_name = identify_generation()
    if gen_name == "BDW":
        return "BDW"
    elif gen_name == "SKL":
        return "SKL"
    elif gen_name in ("BXT", "APL", "GLK"):
        return "BXTx" 
    elif gen_name in ("KBL", "CFL", "WHL", "CML", "AML"):
        return "KBLx"
    elif gen_name == "ICL":
        return "ICL"
    elif gen_name in ("JSL", "EHL"):
        return "EHL/JSL"
    elif gen_name in ("TGL", "RKL", "ADL", "RPL"):
        return "TGLx"
    elif gen_name in ("DG1", "SG1"):
        return "DG1/SG1"
    elif gen_name in ("DG2", "ATSM"):
        return "DG2/ATSM"
    elif gen_name in ("ARL", "MTL"):
        return "MTLx"
    elif gen_name == "LNL":
        return "LNL"
    elif gen_name == "BMG":
        return "BMG"
    elif gen_name == "PTL":
        return "PTL"
    
    