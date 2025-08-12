class VasculatureNetwork:
    """
    Embedded vessel graph with angiogenesis and pruning.

    Parameters
    ----------
    graph : networkx.Graph or similar
        Nodes in 3D; edges for segments.
    domain_shape : tuple[int, int, int]
        Grid shape for mapping to voxels.

    Methods
    -------
    grow(dt_h)
        Tip-cell biased random walk toward VEGF gradients.
    prune(dt_h)
        Remove occluded/low-flow segments.
    map_to_grid()
        Update per-voxel vessel lists and densities.
    """