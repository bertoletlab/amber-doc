class Voxel:
    """
    Container for per-voxel fields and occupancy.

    Attributes
    ----------
    ijk : tuple[int, int, int]
    occupancy : int
        Number of cells currently in the voxel.
    o2 : float
        Oxygen level (arbitrary or mmHg-equivalent).
    vegf : float
        VEGF concentration proxy.
    vessels : list[Vessel]
        Vessel segments intersecting this voxel.
    """