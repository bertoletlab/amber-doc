class Vessel:
    """
    Single vessel segment.

    Attributes
    ----------
    a, b : tuple[float, float, float]
        Endpoints in physical coordinates.
    radius_um : float
    flow : float
        Relative flow used in occlusion/pruning rules.
    is_open : bool
    """