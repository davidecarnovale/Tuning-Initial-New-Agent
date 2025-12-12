import numpy as np

def sliding_entropy_bytes(data, window=64):
    arr = np.frombuffer(data, dtype=np.uint8)
    if len(arr) < window:
        return np.array([])
    out = np.zeros(len(arr) - window + 1)
    for i in range(len(out)):
        w = arr[i:i+window]
        vals, counts = np.unique(w, return_counts=True)
        probs = counts / counts.sum()
        ent = -np.sum(probs * np.log2(probs + 1e-12))
        out[i] = ent
    return out
