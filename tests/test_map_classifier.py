from src.parser.map_classifier import classify_map
import numpy as np

def test_map_classification():
    mat = np.zeros((8,8), dtype=np.uint8)
    result = classify_map(mat)
    assert "eeprom" in [r["type"] for r in result["best"]]
