import json

def detect_vendor(data, vendor_db):
    lowered = data.upper()
    scores = {}
    for vendor, sigs in vendor_db.items():
        score = 0
        for s in sigs:
            if s.upper().encode() in lowered:
                score += 1
        scores[vendor] = score
    best = max(scores.items(), key=lambda x: x[1])
    vendor, score = best
    if score == 0:
        return {"vendor": "unknown", "scores": scores, "confidence": 0.0}
    total = sum(scores.values())
    return {"vendor": vendor, "scores": scores, "confidence": score/total}
