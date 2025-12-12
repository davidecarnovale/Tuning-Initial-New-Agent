import numpy as np
from .entropy import sliding_entropy_bytes
from .stride_detector import best_stride_hint
from .map_classifier import classify_map

def find_regions(data, min_len=384, window=48, ent_thresh_factor=0.85):
    ent = sliding_entropy_bytes(data, window=window)
    if len(ent)==0:
        return []
    ent_norm = (ent - ent.min()) / (ent.max()-ent.min()+1e-12)
    threshold = ent_norm.mean() * ent_thresh_factor
    regions = []
    i = 0
    N = len(ent_norm)
    while i < N:
        if ent_norm[i] < threshold:
            start = i
            while i < N and ent_norm[i] < threshold:
                i += 1
            end = i + window
            start_byte = max(0, start)
            end_byte = min(len(data), end)
            if end_byte - start_byte >= min_len:
                regions.append((start_byte, end_byte))
        else:
            i += 1
    return regions

def analyze_region(data, offset, vendor):
    rb = data[offset[0]:offset[1]]
    hint = best_stride_hint(rb)
    if not hint:
        return {"note": "no stride match", "offset": offset}
    mat = hint["mat"]
    guess = classify_map(mat)
    return {
        "offset": offset,
        "stride": hint["stride"],
        "rows": hint["rows"],
        "cols": mat.shape[1],
        "classification": guess
    }
