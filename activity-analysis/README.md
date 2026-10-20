# Activity analysis privacy boundary

No account activity lists, summaries, laps, GPS traces, heart-rate zones or sensor series are bundled. The historical report-generation scripts embedded a real activity ID and personalized measurements/interpretation and are intentionally omitted rather than relabeled as generic fixtures.

Any future analyzer must accept explicit private inputs, keep run/walk classification separate from user intent, distinguish timer/moving/elapsed duration, avoid assuming uniform sample spacing, and preserve missingness and uncertain sensor/zone calibration. Outputs remain personal health data even after coordinates and owner IDs are removed; keep them outside tracked directories. Workout templates are not completed activities. No personalized fitness inference is made by this repository.
