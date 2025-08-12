Overview
========

AMBER couples an agent-based tumor model with continuum fields (oxygen, VEGF) and a vasculature module; it can ingest dose maps from TOPAS/TOPAS-nBio for radiobiology studies. See the paper for the full model description.

Key ideas
---------
- Voxelized domain; cells divide and move based on crowding and local rules.
- Pre-generated healthy vasculature with angiogenesis toward VEGF gradients; vessels can be pruned/occluded.
- Oxygen distribution per voxel from sub-voxel simulations to mimic chronic hypoxia; acute hypoxia from transient occlusion.
- Radiation response accounts for oxygen effects and heterogeneous dose input.

References
----------
- Kunz LV, Bosque JJ, Nikmaneshi M, Chamseddine I, Munn LL, Schuemann J, Paganetti H, Bertolet A. *AMBER: A Modular Model for Tumor Growth, Vasculature and Radiation Response*. **Bull Math Biol** 86(12):139, 2024. doi:10.1007/s11538-024-01371-4.