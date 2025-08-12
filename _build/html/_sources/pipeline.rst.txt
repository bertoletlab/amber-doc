Simulation pipeline
===================

1. World build
   - Parse CONFIG; create domain, vasculature, and initial tumor state.
2. Dynamics per step
   - Cell cycle, crowding-driven movement, hypoxia/necrosis update.
   - Oxygen and VEGF fields update; angiogenesis/pruning.
3. Radiation events
   - Load dose map; apply survival model (oxygen-aware if configured).
4. Outputs
   - Time series (volume, hypoxic fraction, necrosis), snapshots, logs.