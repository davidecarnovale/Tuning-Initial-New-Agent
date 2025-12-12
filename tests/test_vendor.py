from src.parser.vendor_detector import detect_vendor

def test_vendor_detection():
    data = b"this ECU contains BOSCH signature"
    vendor_db = {
        "bosch":["BOSCH"],
        "siemens":["SIEMENS"]
    }
    result = detect_vendor(data, vendor_db)
    assert result["vendor"] == "bosch"
