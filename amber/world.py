class World:
    """
    Global simulation state constructed from a CONFIG file.

    Parameters
    ----------
    config_path : str or pathlib.Path
        Path to a CONFIG file (e.g., 'CONFIG_LQ.txt').
    overrides : dict, optional
        Key-value overrides applied after parsing the file.
    rng : numpy.random.Generator, optional
        RNG to use; if omitted, created from the 'seed' in CONFIG.

    Attributes
    ----------
    params : dict
        Parsed parameters from CONFIG (and overrides).
    grid : ndarray
        Voxel grid storing per-voxel fields and occupancy.
    vasculature : VasculatureNetwork
        Vessel graph embedded in the domain.
    cells : list[Cell]
        Live cell objects managed by the simulator.
    time_h : float
        Current simulated time in hours.

    Notes
    -----
    World is a pure container. No time-stepping here; use :class:`Simulator`.
    """