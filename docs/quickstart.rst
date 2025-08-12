Quickstart
==========

Minimal run
-----------

.. code-block:: python

   import amber as am

   # Load world from a CONFIG file (see :doc:`configuration`)
   world = am.World(config_path="CONFIG_LQ.txt")

   sim = am.Simulator(world)
   sim.run()  # runs until stopping condition in the CONFIG

   # Inspect outputs or plot
   from amber import plotting
   plotting.plot_timeseries(output_dir="./output/...", vars=["tumor_volume", "hypoxic_fraction"])  # example signature

Command-line (cluster)
----------------------
The repository includes shell helpers to run batches. For example::

   bash run_AMBER.sh example.py <n_iter> CONFIG_LQ

See ``run_AMBER_*.sh`` in the repo for details.