import json

def get_num_active_engines(fname : str) -> int:
    data = read_gputop_json(fname)

    num_engines = 0
    for k, v in data[0]["engines"].items():
        if "Video/" in k and (v.get("busy") is not None):
            num_engines += 1

    return num_engines

# The video engine parameter here 
def compute_time_above_thresh_intel(fname : str, threshold : float, 
        video_engine="Video/") -> float:
    data = read_gputop_json(fname)

    time_above_threshold = 0.0
    for d in data:
        # Get the duration of the measurement
        duration, _ = d["period"].items()
        # Looking at the `engines` section only
        for k, v in d["engines"].items():
            # Focus on GPU usage for video encoding/decoding only
            if video_engine in k and (v.get("busy") is not None) and v["busy"] > threshold:
                time_above_threshold += duration[1]

    return time_above_threshold

def compute_avg_intel(fname : str) -> float:
    data = read_gputop_json(fname)
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

def read_gputop_json(fname : str) -> dict:
    with open(fname, 'r') as f:
        content = f.read().strip()

        # intel_gpu_top -J does not return valid JSON. The brackets are missing.
        if content[0] != "[":
            data = json.loads("[" + content + "]")
        else:
            data = json.loads(content)

    return data
