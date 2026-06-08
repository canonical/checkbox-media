import glob
import re
import urllib.request
from pathlib import Path


TRACE_GLOB = "/tmp/libva.trace*"


def download(url: str, dest: Path) -> None:
    print(f"Downloading {url} ...")
    urllib.request.urlretrieve(url, dest)


def check_hw_acceleration(libva_profile: str, libva_entrypoint: str) -> bool:
    """Return True if the trace files show the expected profile followed by entrypoint."""
    profile_pat = re.compile(rf"profile\s*=\s*{re.escape(libva_profile)}")
    entrypoint_pat = re.compile(rf"entrypoint\s*=\s*{re.escape(libva_entrypoint)}")
    for trace_file in glob.glob(TRACE_GLOB):
        try:
            lines = Path(trace_file).read_text(errors="replace").splitlines()
        except OSError:
            continue
        waiting_for_entrypoint = False
        for line in lines:
            if profile_pat.search(line):
                waiting_for_entrypoint = True
            elif waiting_for_entrypoint and entrypoint_pat.search(line):
                return True
    return False
