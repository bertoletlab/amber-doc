class Cell:
    """
    Agent representing a tumor cell.

    Attributes
    ----------
    id : int
    pos : tuple[int, int, int]
        Voxel indices (i, j, k).
    state : str
        One of {'proliferating', 'quiescent', 'hypoxic', 'necrotic'}.
    age_h : float
        Age since last division.
    o2 : float
        Local oxygen proxy used by radiosensitivity rules.
    alive : bool

    Notes
    -----
    Cell behavior (division, death, movement) is governed by local
    crowding, oxygen, and model parameters in ``World.params``.
    """