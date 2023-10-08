#!/usr/bin/env python3
'''Task 11's module.
'''

from typing import Dict, TypeVar, Optional

K = TypeVar('K')  # TypeVar for the dictionary key
V = TypeVar('V')  # TypeVar for the return value

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> V:
    '''Safely retrieves a value from a dictionary.
    
    Args:
        dct (Dict[K, V]): The dictionary to retrieve the value from.
        key (K): The key to search for in the dictionary.
        default (Optional[V], optional): The default value to return if the key is not found.
    
    Returns:
        V: The value associated with the key in the dictionary, or the default value if not found.
    '''
    if key in dct:
        return dct[key]
    else:
        return default

