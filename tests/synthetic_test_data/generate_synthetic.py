import numpy as np

def generate_synthetic(path="synthetic_ecu.bin"):
    header = b"BOSCH EDC17 SYNTH TEST" + bytes(np.random.randint(0,255,64))
    inj = np.clip(np.random.normal(40, 10, (8,16)), 0, 255).astype(np.uint8)
    rail = np.clip(np.random.normal(200, 15, (12,32)), 0, 255).astype(np.uint8)
    rep = b"\x00\x01\x02\x03" * 200
    with open(path,"wb") as f:
        f.write(header)
        f.write(bytes(np.random.randint(0,255,1024)))
        f.write(inj.tobytes())
        f.write(bytes(np.random.randint(0,255,512)))
        f.write(rail.tobytes())
        f.write(rep)
    return path
