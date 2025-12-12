# Tuning-Initial-New-Agent

# ECU Map Agent

ECU Map Agent is a modular toolkit for parsing, detecting, and classifying ECU maps extracted from automotive control units (Bosch, Siemens, Marelli, Delphi, Denso, etc).

Features:
- Vendor detection
- Map region extraction
- Map type classifier (heuristic)
- CLI analysis tool

Installation:
```
pip install -r requirements.txt
```

Run analysis:
```
python -m src.cli.run_analysis <file.bin>
```

License: MIT
