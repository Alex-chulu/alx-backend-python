#!/usr/bin/env python3

"""
safely_get_value - Safely gets a value from a dictionary.

This function safely retrieves a value from a dictionary by providing a key and an optional default value.
If the key exists in the dictionary, the corresponding value is returned. Otherwise, the default value (which is None by default) is returned.

Parameters:
- dct (dict): The dictionary to retrieve the value from.
- key: The key to look up in the dictionary.
- default (optional): The default value to return if the key is not found. Defaults to None.

Returns:
- The value associated with the given key if it exists in the dictionary, or the default value.

"""

from typing import TypeVar, Dict, Optional

K = TypeVar('K')  # Key type
V = TypeVar('V')  # Value type

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> V:
    if key in dct:
        return dct[key]
    else:
        return default

