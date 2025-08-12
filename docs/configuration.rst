Configuration file
==================

AMBER reads a plain-text ``CONFIG`` file (examples: ``CONFIG_LQ.txt``, ``CONFIG_vasculature_irrad.txt``). The parser expects one key per line, e.g.::

   key = value

Common keys (fill from your CONFIG files)
-----------------------------------------
**Simulation**
- ``dt``: time step (hours)
- ``t_max``: total simulated time
- ``seed``: RNG seed (``-1`` lets AMBER randomize per run)
- ``save_every``: I/O frequency
- ``output_dir``: base output path

**Geometry/voxels**
- ``voxel_size``: linear voxel size (µm or mm; state units here)
- ``domain_shape``: nx,ny,nz or path to a geometry file

**Cells**
- ``proliferation_rate`` (or distribution parameters)
- ``max_crowding``: occupancy threshold for diffusion to neighbors
- ``necrosis_threshold``: long hypoxia → necrosis

**Oxygen/VEGF**
- ``oxygen_model`` and parameters (diffusion, consumption)
- ``vegf_secretion_rate``, ``angiogenesis_rate``

**Vasculature**
- ``vasculature_file``: pre-generated network file
- ``angiogenesis_bias``: bias along VEGF gradient; random-walk params

**Radiation**
- ``dose_map``: path to dose (e.g., from TOPAS)
- ``survival_model``: e.g., ``LQ`` with ``alpha``, ``beta``
- ``OER_model`` and parameters if oxygen modifies radiosensitivity
- ``fractionation_file``: CSV with schedule (``FRAC_*.csv`` provided)

**Stopping criteria**
- ``max_steps`` or ``tumor_volume_target``

.. include:: _autogen/config_schema.rst

Notes
-----
- Use the provided CONFIG examples as a template and document any lab-specific keys.
- For sweeps on clusters, the run scripts allow key overrides per iteration.