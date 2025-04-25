#!/usr/bin/env python3
"""
Module for to_kv function: returns a tuple with a string
and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and the square of v as a float."""
    return (k, float(v ** 2))
