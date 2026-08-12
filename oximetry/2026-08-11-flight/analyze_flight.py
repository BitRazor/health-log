#!/usr/bin/env python3
"""In-flight SpO2/pulse analysis for a Checkme O2 Max recording.

Timeline per user: recording starts 19:07 on the ground; aircraft began
the flight (takeoff/climb) at ~19:50; recording stopped mid-flight.
"""
import csv
import statistics
from datetime import datetime

CSV_FILE = "Checkme O2 Max 603891_20260811190725.csv"
TAKEOFF = "19:50:00"


def load(path):
    rows = []
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            spo2, pulse = r["Oxygen Level"].strip(), r["Pulse Rate"].strip()
            if not spo2.isdigit() or not pulse.isdigit():
                continue
            t = datetime.strptime(r["Time"], "%H:%M:%S %d/%m/%Y")
            rows.append((t, int(spo2), int(pulse), int(r["Motion"])))
    return rows


def stats(rows, label):
    s = [x[1] for x in rows]
    p = [x[2] for x in rows]
    dur = (rows[-1][0] - rows[0][0]).total_seconds() / 60
    below = {th: 2 * sum(1 for v in s if v < th) / 60 for th in (94, 90, 88)}
    print(f"\n{label}: {rows[0][0]:%H:%M:%S}-{rows[-1][0]:%H:%M:%S} "
          f"({dur:.0f} min, n={len(rows)})")
    print(f"  SpO2 mean {statistics.mean(s):.1f} / median "
          f"{statistics.median(s):.0f} / min {min(s)} / max {max(s)}")
    print(f"  time below 94%: {below[94]:.1f} min | below 90%: "
          f"{below[90]:.1f} min | below 88%: {below[88]:.1f} min")
    print(f"  Pulse mean {statistics.mean(p):.1f} / median "
          f"{statistics.median(p):.0f} / min {min(p)} / max {max(p)}")


def main():
    rows = load(CSV_FILE)
    t_off = datetime.strptime(f"{TAKEOFF} 11/08/2026", "%H:%M:%S %d/%m/%Y")
    ground = [r for r in rows if r[0] < t_off]
    flight = [r for r in rows if r[0] >= t_off]

    print(f"recording {rows[0][0]:%H:%M:%S}-{rows[-1][0]:%H:%M:%S}, "
          f"{len(rows)} valid samples")
    stats(ground, "GROUND (pre-flight)")
    stats(flight, "FLIGHT (from 19:50)")

    # 5-minute profile through the whole recording
    print("\n5-min blocks (time, SpO2 mean/min, pulse mean):")
    t0 = rows[0][0]
    block = 0
    while True:
        w = [r for r in rows
             if 300 * block <= (r[0] - t0).total_seconds() < 300 * (block + 1)]
        if not w:
            break
        s = [x[1] for x in w]
        p = [x[2] for x in w]
        tag = " <-- flight" if w[0][0] >= t_off and w[0][0] < t_off.replace(minute=55) else ""
        print(f"  {w[0][0]:%H:%M} {statistics.mean(s):5.1f}/{min(s):2d}  "
              f"{statistics.mean(p):5.1f}")
        block += 1

    # lowest sustained SpO2: worst 60 s rolling mean during flight
    fs = [x[1] for x in flight]
    worst, wi = 101, 0
    for i in range(len(fs) - 30):
        m = sum(fs[i:i + 30]) / 30
        if m < worst:
            worst, wi = m, i
    print(f"\nworst 60 s in flight: mean SpO2 {worst:.1f}% at "
          f"{flight[wi][0]:%H:%M:%S}")


if __name__ == "__main__":
    main()
