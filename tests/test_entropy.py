from src.parser.entropy import sliding_entropy_bytes
import numpy as np

def test_entropy_basic():
    data = b"\x00"*100
    ent = sliding_entropy_bytes(data)
    assert ent.mean() < 1
