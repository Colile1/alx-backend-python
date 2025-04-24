#!/usr/bin/env python3
"""
Module for safe_first_element function: returns the first element or None.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst if it exists, else None."""
    if lst:
        return lst[0]
    else:
        return None
