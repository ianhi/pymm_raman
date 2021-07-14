from ._version import __version__

from typing import Dict, List, Tuple
from mpl_point_clicker import clicker
import xarray as xr
import numpy as np
from collections import defaultdict


def clickers_to_xarray(
    clickers: List[clicker],
    classes: List[str],
    S: int,
    T: int,
    wavenumbers: np.ndarray = None,
) -> Tuple[xr.Dataset, xr.Dataset]:
    """
    Convert a list of clickers to datasets of coords and datastorage.

    Parameters
    ----------
    clickers : list of clickers
    classes : list of str
        The names of the classes
    S, T : int
        The number of positions and time points respectively.
    wavenumbers : arraylike of float, optional
        The coordinates to be used for the rm on the DataArray

    Returns
    -------
    rm_aim_ds : xr.Dataset
        The coordinates for aiming
    rm_data_ds : xr.Dataset
        A dataset for storing the spectra
    """
    if len(clickers) != S:
        raise ValueError(
            "Not as many clickers as positions. Add None to not use a position."
        )
    if wavenumbers is None:
        wavenumbers = np.arange(1340)

    rm_data_ds = xr.Dataset()
    rm_aim_ds = xr.Dataset()
    max_spec = {c: 0 for c in classes}
    T = 5
    class_positions = defaultdict(lambda: list())
    for c in clickers:
        if c is None:

            continue
        pos = c.get_positions()
        for k, v in pos.items():
            class_positions[k].append(v)
            if len(v) > max_spec[k]:
                max_spec[k] = len(v)
    for klass, max_ in max_spec.items():
        # TODO
        # TODO
        # TODO
        # TODO
        # TODO
        ###################
        # Add in the conversion to galvo coords
        ###################
        # TODO
        # TODO
        # TODO
        # TODO
        # TODO
        rm_aim_ds[klass] = xr.DataArray(
            -np.ones((S, max_, 2)), dims=("S", f"{klass}_spec", "spec_xy")
        )
        rm_data_ds[klass] = xr.DataArray(
            -np.ones((S, T, max_, 1340), dtype=int),
            dims=("S", "T", f"{klass}_spec", "wns"),
            coords={"wns": wavenumbers},
        )
        jagged = class_positions[klass]
        for i, arr in enumerate(jagged):
            if len(arr) != 0:
                rm_aim_ds[klass].values[i, : len(arr)] = arr
    return rm_aim_ds, rm_data_ds


__all__ = [
    "clickers_to_xarray",
    "__version__",
]
