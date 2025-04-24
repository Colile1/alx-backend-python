#!/usr/bin/env python3
"""Module for zoom_array function: returns a list with each item repeated."""

from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list with each item in lst repeated factor times."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
