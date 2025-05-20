#!/usr/bin/env python3
"""
Utility functions for nested map access, HTTP JSON fetching, and memoization.
"""
from typing import Mapping, Any, Tuple, Sequence, Callable
import requests


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a value in a nested map using a sequence of keys.
    Args:
        nested_map: A dictionary potentially containing nested dictionaries.
        path: A sequence of keys to traverse the nested_map.
    Returns:
        The value found at the end of the path.
    Raises:
        KeyError: If a key in the path does not exist.
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Any:
    """
    Fetch JSON content from a URL.
    Args:
        url: The URL to fetch JSON from.
    Returns:
        The parsed JSON response.
    """
    response = requests.get(url)
    return response.json()


def memoize(method: Callable) -> Callable:
    """
    Decorator to cache the result of a method call as a property.
    Args:
        method: The method to memoize.
    Returns:
        The memoized property.
    """
    attr_name = "_memoized_" + method.__name__

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)
    return wrapper
