#!/usr/bin/env python3
"""Basic type annotated function"""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """Str to Int|Float function"""
    return (k, v * v)
