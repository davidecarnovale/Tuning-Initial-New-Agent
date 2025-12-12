from src.parser.stride_detector import best_stride_hint
import numpy as np

def test_stride_hint():
    mat = np.arange(64, dtype=np.uint8)
    arr = mat.tobytes()
    hint = best_stride_hint(arr, min_rows=2)
    assert hint is not None
    assert hint["stride"] in [8,16,32,64]
