#!/usr/bin/env python3
"""Orthostatic (lying -> standing) pulse analysis for a Checkme O2 Max recording.

Protocol applied per request:
  - discard the first 30 s (sensor settling)
  - detect the stand-up moment from the sharp sustained pulse rise
  - discard the transition window around the stand-up (the rise itself)
  - compare supine baseline vs standing steady state
"""
import csv
import statistics
import sys
from datetime import datetime

CSV_FILE = "Checkme O2 Max 603891_20260811065114.csv"
SETTLE_CUT_S = 30          # seconds removed from start
TRANSITION_CUT_S = 30      # seconds removed starting at stand-up


def load(path):
    rows = []
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            spo2, pulse = r["Oxygen Level"].strip(), r["Pulse Rate"].strip()
            if not spo2.isdigit() or not pulse.isdigit():
                continue  # sensor-off rows ("- -") at the tail
            t = datetime.strptime(r["Time"], "%H:%M:%S %d/%m/%Y")
            rows.append((t, int(spo2), int(pulse), int(r["Motion"])))
    return rows


def detect_standup(rows):
    """First index where pulse jumps >=15 bpm within 10 s and stays >=20 bpm
    above the preceding 60 s median for the following 30 s."""
    for i in range(30, len(rows) - 15):
        base = statistics.median(p for _, _, p, _ in rows[max(0, i - 30):i])
        if rows[i + 5][2] - rows[i][2] >= 15:
            nxt = [p for _, _, p, _ in rows[i + 5:i + 20]]
            if statistics.mean(nxt) - base >= 20:
                return i
    return None


def seg_stats(rows):
    p = [x[2] for x in rows]
    s = [x[1] for x in rows]
    return {
        "n": len(rows), "start": rows[0][0], "end": rows[-1][0],
        "hr_mean": statistics.mean(p), "hr_med": statistics.median(p),
        "hr_min": min(p), "hr_max": max(p),
        "spo2_mean": statistics.mean(s), "spo2_min": min(s),
    }


def fmt(seg, label):
    d = (seg["end"] - seg["start"]).total_seconds()
    return (f"{label}: {seg['start']:%H:%M:%S}-{seg['end']:%H:%M:%S} "
            f"({d/60:.1f} min, n={seg['n']})\n"
            f"  HR mean {seg['hr_mean']:.1f} / median {seg['hr_med']:.0f} "
            f"/ min {seg['hr_min']} / max {seg['hr_max']} bpm\n"
            f"  SpO2 mean {seg['spo2_mean']:.1f}% / min {seg['spo2_min']}%")


def main():
    rows = load(CSV_FILE)
    t0 = rows[0][0]
    kept = [r for r in rows if (r[0] - t0).total_seconds() >= SETTLE_CUT_S]

    i_up = detect_standup(kept)
    if i_up is None:
        sys.exit("no stand-up transition found")
    t_up = kept[i_up][0]

    supine = [r for r in kept if r[0] < t_up]
    standing = [r for r in kept
                if (r[0] - t_up).total_seconds() >= TRANSITION_CUT_S]
    transition = [r for r in kept
                  if 0 <= (r[0] - t_up).total_seconds() < TRANSITION_CUT_S]

    sup, sta = seg_stats(supine), seg_stats(standing)
    print(f"recording {t0:%H:%M:%S}-{rows[-1][0]:%H:%M:%S %d/%m/%Y}, "
          f"{len(rows)} valid samples @2 s")
    print(f"cut: first {SETTLE_CUT_S} s; stand-up detected at {t_up:%H:%M:%S}; "
          f"transition cut {t_up:%H:%M:%S}+{TRANSITION_CUT_S} s")
    print(fmt(sup, "SUPINE (baseline)"))
    print(fmt(sta, "STANDING (steady state)"))
    tr_p = [x[2] for x in transition]
    print(f"TRANSITION (excluded): peak {max(tr_p)} bpm")

    d_mean = sta["hr_mean"] - sup["hr_mean"]
    d_med = sta["hr_med"] - sup["hr_med"]
    print(f"\nDELTA HR: mean +{d_mean:.1f} bpm, median +{d_med:.0f} bpm")

    # sustained HR per minute after standing (from t_up, transition included
    # in the timeline but minute windows start after the cut)
    print("\nper-minute standing means (from stand-up):")
    for m in range(1, 11):
        win = [x[2] for x in kept
               if 60 * (m - 1) <= (x[0] - t_up).total_seconds() < 60 * m]
        if win:
            print(f"  min {m:2d}: {statistics.mean(win):5.1f} bpm "
                  f"(delta +{statistics.mean(win)-sup['hr_med']:.1f})")


if __name__ == "__main__":
    main()
