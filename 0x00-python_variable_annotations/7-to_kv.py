#!/usr/bin/env python3
"""Basic type annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Str to Int|Float function"""
    return (k, v * v)
