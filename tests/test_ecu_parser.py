from src.parser.ecu_parser import find_regions, analyze_region
from src.parser.vendor_detector import detect_vendor

def test_parser_basic():
    data = b"\x00"*1000
    regions = find_regions(data, min_len=128, window=16)
    assert isinstance(regions, list)
    vendor = {"vendor":"unknown"}
    for r in regions:
        result = analyze_region(data, r, vendor)
        assert "offset" in result
