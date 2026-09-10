# Evening oximetry — 2026-08-16 19:38–23:15

Device: Checkme O2 Max (SN 603891), 2-second sampling.
Source: `Checkme O2 Max 603891_20260816193831.csv` — 6,491 valid samples, 2 dropped.
Context (from the session message, not the export): started ~1 h after the
bike session; eating, a ~10 min walk, then mostly gaming.

## ⚠ Finding: sustained desaturation while seated

**SpO2 drifted to 88% and held 12.6 minutes (20:07:31–20:20:07), nadir 86%,
with the motion sensor reading zero on most samples.** Total time below 90%
across the recording: 15.2 min (7.0%). This is the first objective
desaturation in the recordings analysed to date.

### Artefact controls — all four point the same way

| Check | Reading |
|---|---|
| Same-session control (motion-free samples only, same device/finger) | before 96.3% → **during 91.1%** → after 96.7% |
| Motion channel through the 12.6-min plateau | zero on most samples, max value 9 |
| Trace smoothness across recording | 90% of 2 s steps unchanged, 0.2% moved ≥3% |
| Shape | 9-min glide down, flat plateau, 30 s recovery |

The device demonstrably read 96–97% on both sides of the event under the same
conditions, so this is not a systematically low-reading sensor.

**Separately: the two dips during the walk ARE artefact** — 19:41 (nadir 80%)
and 19:44 (nadir 86%), both with the accelerometer saturated (motion 100%
active, values 22–24). Ignore those two.

## Phase table

| Window | Activity | SpO2 mean | SpO2 min | Pulse mean | Motion active |
|---|---|---|---|---|---|
| 19:38–19:48 | Walk | 92.0% | 80%* | 100 bpm | 97% |
| 19:48–20:02 | Settling, seated | 96.3% | 93% | 83 bpm | 18% |
| **20:02–20:40** | **Seated — event window** | **91.2%** | **86%** | 94 bpm | 33% |
| 20:40–21:08 | Seated, saturation restored | 96.1% | 91% | 103 bpm | 48% |
| 21:08–23:15 | Evening, seated | 96.5% | 89% | 84 bpm | 19% |

\* movement artefact, not a real value

## Interpretation (not a diagnosis)

The kinetics — slow glide down, flat plateau, rapid recovery — are the
signature of **reduced ventilation**, not a circulatory or sensor problem.
Pulse stayed 74–95 through the plateau, i.e. no compensatory tachycardia.

Three ordinary contributors plausibly combine to explain a drift to 88–89%:
absorbed shallow breathing during concentrated screen use; slouched seated
posture reducing functional lung volume; and a recent meal raising the
diaphragm. Nonetheless a sustained 12-minute desaturation while awake and at
rest sits outside the normal range and should not be filed away on the
strength of a plausible story alone.

Note also: pulse ran 100–120 bpm seated from 20:22 to ~21:05 (small hand
movements only), ~2 h after the bike session. Gaming arousal is the ordinary
explanation; recorded here because it overlaps the second half of the window.

## Next steps

1. **Repeat the conditions** — another gaming session with the oximeter on,
   same seating. Reproducible or one-off?
2. **Test the posture hypothesis** — when SpO2 next reads <91%, sit up
   straight and take ten slow deep breaths. Recovery within a minute confirms
   the ventilation mechanism.
3. **Cross-check the device once** against a clinical oximeter at any
   appointment — settles both this and the open question of whether the unit
   reads low.
4. **Raise with the clinician.** "Repeat oximetry" is already on the
   never-done list, and the 2023 sleep study's central/obstructive split is
   unresolved. A daytime awake desaturation is relevant to both.

## Files

- `Checkme O2 Max 603891_20260816193831.csv` — raw export
- `report.html` — full formatted report with charts (open in a browser)
