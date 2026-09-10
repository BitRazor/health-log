#!/usr/bin/env python3
"""Overnight oximetry analysis for a Checkme O2 Max recording.

Computes the standard screening metrics used for nocturnal oximetry:
  ODI3 / ODI4  - oxygen desaturation index, events per hour
  T90/T88/T85  - time spent below each saturation threshold
  event detail - depth, duration and clustering of desaturations

Desaturation scoring follows the usual convention: from a stable pre-event
baseline, a fall of >=N% lasting >=10 s that then recovers toward baseline.
"""
import csv
import statistics
from datetime import datetime

CSV_FILE = "Checkme O2 Max 603891_20260909235020.csv"


def load(path):
    rows, dropped = [], 0
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            spo2, pulse = r["Oxygen Level"].strip(), r["Pulse Rate"].strip()
            if not spo2.isdigit() or not pulse.isdigit():
                dropped += 1
                continue
            t = datetime.strptime(r["Time"], "%H:%M:%S %d/%m/%Y")
            rows.append((t, int(spo2), int(pulse), int(r["Motion"])))
    return rows, dropped


def desaturations(rows, drop=3, min_dur=10, max_dur=180, sample_s=2):
    """Score desaturation events against a rolling stable baseline.

    An event starts when SpO2 falls >=`drop`% below the local baseline and ends
    when it recovers to within 1% of that baseline. Events are capped at
    `max_dur` so a slow overnight drift cannot merge into one huge pseudo-event.
    """
    spo2 = [r[1] for r in rows]
    n = len(spo2)
    base_win = 60 // sample_s * 2          # 2 minutes of samples
    cap = max_dur // sample_s
    events = []
    i = base_win
    while i < n - 1:
        # baseline = typical of the highest third of the preceding window
        base = statistics.median(sorted(spo2[i - base_win:i])[-base_win // 3:])
        if spo2[i] <= base - drop:
            j, nadir = i, spo2[i]
            limit = min(n, i + cap)
            while j < limit and spo2[j] <= base - 1:
                nadir = min(nadir, spo2[j])
                j += 1
            dur = (j - i) * sample_s
            recovered = j < limit           # ended by recovery, not by the cap
            if min_dur <= dur and base - nadir >= drop:
                seg = rows[i:j] or rows[i:i + 1]
                events.append({
                    "start": rows[i][0], "end": rows[min(j, n - 1)][0],
                    "base": base, "nadir": nadir, "depth": base - nadir,
                    "dur": dur, "recovered": recovered,
                    "hr_lo": min(r[2] for r in seg),
                    "hr_hi": max(r[2] for r in seg),
                    "motion": max(r[3] for r in seg),
                })
                i = j
                continue
        i += 1
    return events


def main():
    rows, dropped = load(CSV_FILE)
    t0, t1 = rows[0][0], rows[-1][0]
    hours = (t1 - t0).total_seconds() / 3600
    spo2 = [r[1] for r in rows]
    pulse = [r[2] for r in rows]
    motion = [r[3] for r in rows]

    print(f"RECORDING  {t0:%H:%M:%S %d/%m} -> {t1:%H:%M:%S %d/%m}")
    print(f"  duration {hours:.2f} h | valid {len(rows)} | dropped {dropped}")

    print(f"\nSATURATION")
    print(f"  mean {statistics.mean(spo2):.1f}%  median {statistics.median(spo2):.0f}%"
          f"  min {min(spo2)}%  max {max(spo2)}%")
    for th in (95, 94, 92, 90, 88, 85, 80):
        n = sum(1 for v in spo2 if v < th)
        print(f"  below {th}%: {2*n/60:7.1f} min ({100*n/len(spo2):5.1f}% of night)")

    print(f"\nPULSE")
    print(f"  mean {statistics.mean(pulse):.1f}  median {statistics.median(pulse):.0f}"
          f"  min {min(pulse)}  max {max(pulse)}")
    print(f"\nMOTION  active on {100*sum(1 for m in motion if m>0)/len(motion):.0f}% of samples")

    for drop in (3, 4):
        ev = desaturations(rows, drop=drop)
        odi = len(ev) / hours
        sev = ("normal" if odi < 5 else "mild" if odi < 15
               else "moderate" if odi < 30 else "severe")
        print(f"\nODI{drop}  {odi:.1f} events/hour   ({len(ev)} events)   -> {sev} range")
        if ev:
            print(f"  depth  mean {statistics.mean([e['depth'] for e in ev]):.1f}%"
                  f"  max {max(e['depth'] for e in ev)}%")
            print(f"  length mean {statistics.mean([e['dur'] for e in ev]):.0f}s"
                  f"  max {max(e['dur'] for e in ev)}s")
            print(f"  lowest nadir {min(e['nadir'] for e in ev)}%")

    ev3 = desaturations(rows, drop=3)
    print(f"\nHOURLY BREAKDOWN")
    print(f"  hour        SpO2 mean/min   T90(min)  ODI3   pulse mean  motion")
    h = 0
    while True:
        w = [r for r in rows if 3600*h <= (r[0]-t0).total_seconds() < 3600*(h+1)]
        if not w:
            break
        ss = [x[1] for x in w]
        t90 = 2*sum(1 for v in ss if v < 90)/60
        n_ev = sum(1 for e in ev3 if 3600*h <= (e["start"]-t0).total_seconds() < 3600*(h+1))
        span = len(w)*2/3600
        print(f"  {w[0][0]:%H:%M}-{w[-1][0]:%H:%M}  {statistics.mean(ss):5.1f}/{min(ss):3d}"
              f"     {t90:6.1f}   {n_ev/span if span else 0:5.1f}"
              f"      {statistics.mean([x[2] for x in w]):5.1f}"
              f"    {100*sum(1 for x in w if x[3]>0)/len(w):3.0f}%")
        h += 1

    deep = sorted([e for e in ev3 if e["depth"] >= 4],
                  key=lambda e: e["nadir"])[:15]
    if deep:
        print(f"\nDEEPEST EVENTS (>=4% drop, worst 15 by nadir)")
        for e in deep:
            print(f"  {e['start']:%H:%M:%S}  {e['base']:.0f}% -> {e['nadir']}%"
                  f"  (-{e['depth']:.0f})  {e['dur']:3.0f}s"
                  f"  pulse {e['hr_lo']}-{e['hr_hi']}  motion max {e['motion']}")


if __name__ == "__main__":
    main()
