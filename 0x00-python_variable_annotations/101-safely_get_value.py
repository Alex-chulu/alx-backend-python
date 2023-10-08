#!/usr/bin/env python3
'''Task 11's module.
'''

from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Safely retrieves a value from a dictionary.
    
    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to search for in the dictionary.
        default (Def, optional): The default value to return if the key is not found.
    
    Returns:
        Res: The value associated with the key in the dictionary, or the default value if not found.
    '''
    if key in dct:
        return dct[key]
    else:
        return default

