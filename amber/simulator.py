class Simulator:
    """
    Main simulation driver operating on a :class:`World`.

    Parameters
    ----------
    world : World
        Initialized world.
    max_steps : int, optional
        Hard cap on steps (in addition to any stopping criteria).
    log_dir : str or Path, optional
        Output directory; falls back to world.params['output_dir'].

    Methods
    -------
    run()
        Advance until a stopping condition is met.
    step()
        Single step: update cells, fields (O2/VEGF), and vasculature.
    schedule_radiation(event)
        Queue a radiation event (dose map, time, fractionation).
    apply_radiation(event)
        Apply survival model to cells using OER if configured.

    Raises
    ------
    RuntimeError
        If invariants are violated (e.g., negative occupancy).
    """