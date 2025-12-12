import numpy as np

def classify_map(mat):
    stats = {
        "min": int(mat.min()),
        "max": int(mat.max()),
        "mean": float(mat.mean()),
        "std": float(mat.std()),
        "rows": mat.shape[0],
        "cols": mat.shape[1],
        "sparsity": float(np.mean(mat==0)),
        "grad_row": float(np.mean(np.abs(np.diff(mat.astype(np.int16), axis=0)))),
        "grad_col": float(np.mean(np.abs(np.diff(mat.astype(np.int16), axis=1)))),
    }

    scores = {"rail":0.0, "turbo":0.0, "injection":0.0, "torque":0.0, "limiter":0.0, "eeprom":0.0}

    if stats["sparsity"] > 0.6 or stats["std"] < 5:
        scores["eeprom"] += 0.6
    if stats["max"] > 180 and stats["std"] > 20:
        scores["rail"] += 0.5
    if stats["cols"] <= 64 and stats["rows"] <= 64 and stats["grad_row"] < 15:
        scores["turbo"] += 0.4
    if stats["mean"]<80 and stats["std"]>8:
        scores["injection"] += 0.4
    if stats["cols"]>=32 and stats["rows"]>=8 and stats["std"]>10:
        scores["torque"] += 0.4
    if stats["cols"]<=8 or stats["rows"]<=4:
        scores["limiter"] += 0.5

    total = sum(scores.values()) + 1e-9
    for k in scores:
        scores[k] /= total

    best = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return {"stats": stats, "scores": scores, "best": best[:3]}
