# Orthostatic pulse test — 2026-08-11 06:51

Device: Checkme O2 Max (SN 603891), 2-second sampling.
Source: `Checkme O2 Max 603891_20260811065114.csv` (Google Drive upload 2026-08-11).

## Protocol applied

- Recording 06:51:14 → 07:10:10 (~19 min, 569 valid samples).
- **Cut 1:** first 30 s discarded (sensor settling; pulse read 85 → 61 while the reading stabilised).
- Stand-up detected automatically at **07:00:22** (pulse 54 → 88 within 8 s).
- **Cut 2:** 30 s transition window around the stand-up discarded.

## Results

| Segment | Window | Duration | HR mean | HR median | HR min–max | SpO2 mean (min) |
|---|---|---|---|---|---|---|
| Lying down (baseline) | 06:51:44–07:00:12 | 8.5 min | 56.2 | **55** | 51–66 | 95.2% (92%) |
| Standing (steady state) | 07:00:44–07:10:10 | 9.4 min | 89.3 | **89** | 83–99 | 96.2% (93%) |

**Sustained pulse rise on standing: +33 bpm (mean) / +34 bpm (median).**

Per-minute standing means (delta vs supine median 55):

| Min after standing | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| HR (bpm) | 83 | 89 | 91 | 90 | 90 | 90 | 87 | 88 | 89 | 90 |
| Delta | +28 | +34 | +36 | +35 | +35 | +35 | +32 | +33 | +34 | +35 |

## Interpretation notes (not a diagnosis)

- The rise is **immediate and sustained**: it does not decay back toward baseline
  over 10 minutes of standing — it holds at ~+34 bpm throughout.
- A sustained increase of **≥30 bpm within 10 min of standing** (without
  orthostatic hypotension) is the adult heart-rate criterion used in
  POTS / orthostatic-intolerance workups. This single home test meets that
  HR threshold; a pulse oximeter cannot measure blood pressure, and the
  criterion also requires symptoms and reproducibility, so this is a data
  point to bring to a clinician, not a diagnosis.
- Absolute standing HR stays ~83–99 bpm (does not exceed 100).
- SpO2 stayed normal throughout (never below 92%, mostly 95–97%) — no
  desaturation on standing.
- Comparison: the earlier test on 2026-08-02 15:01 (same protocol, two
  cycles) showed supine ~59 → standing ~88 bpm (~+29), and second cycle
  supine ~54 → standing ~90 (~+36). Today's result is consistent, so the
  finding reproduces across days and times of day.

## Files

- `Checkme O2 Max 603891_20260811065114.csv` — raw export
- `analyze.py` — segmentation + stats (prints the numbers above)
- `plot.py` → `orthostatic-2026-08-11.png` — annotated chart
