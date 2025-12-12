import numpy as np

COMMON_STRIDES = [8, 16, 32, 48, 64, 96, 128, 256]

def best_stride_hint(region_bytes, min_rows=3):
    arr = np.frombuffer(region_bytes, dtype=np.uint8)
    best = None
    for stride in COMMON_STRIDES:
        if len(arr) < stride * min_rows:
            continue
        rows = len(arr)//stride
        mat = arr[:rows*stride].reshape((rows, stride))
        col_var = np.var(mat, axis=0).mean()
        row_smooth = np.mean(np.abs(np.diff(mat.astype(np.int16), axis=0))) + 1e-9
        score = float(col_var) / float(row_smooth)
        if best is None or score > best["score"]:
            best = {"stride": stride, "rows": rows, "score": score, "mat": mat}
    return best
