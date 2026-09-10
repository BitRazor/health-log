#!/usr/bin/env python3
"""Chart for the 2026-08-11 in-flight recording."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from analyze_flight import load, CSV_FILE, TAKEOFF

rows = load(CSV_FILE)
t_off = datetime.strptime(f"{TAKEOFF} 11/08/2026", "%H:%M:%S %d/%m/%Y")
t = [r[0] for r in rows]
spo2 = [r[1] for r in rows]
hr = [r[2] for r in rows]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True,
                               height_ratios=[3, 2])

ax1.axvspan(t[0], t_off, color="#4c72b0", alpha=0.08)
ax1.axvspan(t_off, t[-1], color="#dd8452", alpha=0.10)
ax1.plot(t, spo2, color="#4c72b0", lw=1.0)
ax1.axhline(94, color="#888", ls=":", lw=1)
ax1.axhline(90, color="#c44e52", ls="--", lw=1)
ax1.axvline(t_off, color="k", ls="--", lw=1)
ax1.annotate("takeoff 19:50", (t_off, 99.5), xytext=(6, 0),
             textcoords="offset points", fontsize=9)
ax1.text(t[0] + timedelta(minutes=8), 86.6, "GROUND / boarding",
         fontsize=10, color="#33507a", weight="bold")
ax1.text(t_off + timedelta(minutes=25), 86.6,
         "CRUISE — cabin altitude effect (median 92%)",
         fontsize=10, color="#9a5320", weight="bold")
ax1.set_ylim(86, 101)
ax1.set_ylabel("SpO2 (%)")
ax1.grid(alpha=0.3)
ax1.set_title("Checkme O2 Max — flight 2026-08-11 19:07-21:22 "
              "(ground median 96% -> cruise median 92%, min 88%)")

ax2.axvspan(t[0], t_off, color="#4c72b0", alpha=0.08)
ax2.axvspan(t_off, t[-1], color="#dd8452", alpha=0.10)
ax2.plot(t, hr, color="#c44e52", lw=0.9)
ax2.axvline(t_off, color="k", ls="--", lw=1)
ax2.set_ylabel("Pulse (bpm)")
ax2.set_ylim(40, 130)
ax2.grid(alpha=0.3)
ax2.annotate("boarding/walking ~92 bpm", (t[300], 118), fontsize=9,
             color="#883333")
ax2.annotate("seated cruise ~74 bpm", (t_off + timedelta(minutes=35), 108),
             fontsize=9, color="#883333")

ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
fig.tight_layout()
fig.savefig("flight-2026-08-11.png", dpi=140)
print("saved flight-2026-08-11.png")
