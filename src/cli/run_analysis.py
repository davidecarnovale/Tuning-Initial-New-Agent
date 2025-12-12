import json
import os
from pathlib import Path
from ..parser.vendor_detector import detect_vendor
from ..parser.ecu_parser import find_regions, analyze_region

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m src.cli.run_analysis <file.bin>")
        return
    infile = sys.argv[1]
    with open("src/db/vendor_signatures.json") as f:
        vendor_db = json.load(f)

    with open(infile, "rb") as f:
        data = f.read()

    vendor = detect_vendor(data, vendor_db)
    regions = find_regions(data)

    outdir = Path("analysis_output")
    outdir.mkdir(exist_ok=True)

    results = {"file": os.path.basename(infile), "vendor": vendor, "regions": []}

    for idx, region in enumerate(regions):
        info = analyze_region(data, region, vendor)
        info["index"] = idx
        results["regions"].append(info)

    with open(outdir/"analysis.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Analysis saved to", outdir/"analysis.json")

if __name__ == "__main__":
    main()
