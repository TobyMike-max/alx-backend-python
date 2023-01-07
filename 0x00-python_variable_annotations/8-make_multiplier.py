#!/usr/bin/env python3
"""Complex type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Nested function make_multiplier"""
    def fn(num: float):
        return num * multiplier
    return fn
