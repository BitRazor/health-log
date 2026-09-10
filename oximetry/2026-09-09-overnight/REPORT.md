# Overnight oximetry — night of 2026-09-09/10, 23:50–07:04

Device: Checkme O2 Max (SN 603891), 2-second sampling.
Source: `Checkme O2 Max 603891_20260909235020.csv` — 13,019 valid samples, 1 dropped.
Duration 7 h 14 min. Motion active on 6% of samples.

## Result: a reassuring night

**Time below 90%: 0.4 min (24 seconds) — 0.1% of the night.** That is the single
most informative overnight-oximetry metric and it is comfortably normal
(threshold: <1% of the night).

| Metric | This night | Normal band | Verdict |
|---|---|---|---|
| Time below 90% (T90) | 0.4 min · 0.1% | <1% of night | Normal |
| Mean saturation | 95.1% (median 95%) | ≥94% | Normal |
| Lowest reading | 87% | — | Two brief dips |
| ODI4 (drops ≥4%/h) | 4.1 /h | <5 | Normal |
| ODI3 (drops ≥3%/h) | 8.2 /h | <5 | Mild band |
| Sleeping pulse | 54 bpm (46–99) | — | Low and steady |

ODI3 is the only metric outside its band and the softest of them — counting
every 3% dip makes it sensitive to the ±1% sensor flicker. Events behind that
number average 4.2% deep and 68 s long; the stricter ODI4 is normal.

## Why this does not look like sleep apnea

1. **No cyclic heart-rate variation** — the hallmark apnea leaves in oximetry.
   Minute-to-minute pulse varied by only **2.4 bpm** across the night, moving
   ≥8 bpm on 11 of 433 minutes. Only 14 of 59 dips carried a ≥10 bpm pulse rise.
2. **Dips are scattered, not periodic** — median gap between events 2.8 min.
   Apnea produces tightly packed runs at roughly one event per minute.
3. **Movement explains most of the deep dips** — of the ten dips reaching ≤90%,
   **six had a motion spike within ±60 s**. Both 87% readings were immediately
   preceded by a pulse jump (to 85 and 80 bpm against a 53 bpm baseline) while
   saturation was still 96–97% — the signature of a disturbed probe, not a
   breathing event.

## The comparison worth keeping

| Recording | State | Duration | Time <90% | Per hour |
|---|---|---|---|---|
| 9–10 Sep | Asleep | 7.2 h | 0.4 min | 0.06 min/h |
| 16 Aug evening | Awake, seated | 3.6 h | 15.2 min | 4.2 min/h |

A whole night asleep produced roughly **one seventieth** the desaturation per
hour of the awake seated evening. Sleep is not when the desaturation happens —
which points further toward the awake postural/breathing-pattern explanation
for the 16 August event and away from a sleep-breathing cause spilling into
the day.

## Limits

- **A screen, not a sleep study.** Saturation and pulse only — no airflow,
  effort or EEG. It **cannot separate central from obstructive events**, and
  cannot detect apneas ending in arousal without measurable desaturation. The
  2023 sleep study question stays open; this narrows it rather than closing it.
- **One night.** Sleep-disordered breathing varies with position, alcohol,
  congestion and sleep stage. A clean night lowers the probability of a
  significant problem; it does not exclude one.
- **Not a diagnosis.** Consumer oximeter, ±2% stated accuracy; the open question
  of whether this unit reads low still stands.

## Files

- `Checkme O2 Max 603891_20260909235020.csv` — raw export
- `analyze_overnight.py` — ODI/T90 scoring and hourly breakdown
- `report.html` — full formatted report with charts
