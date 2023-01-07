#!/usr/bin/env python3
"""Basic type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """List Summer function"""
    return sum(input_list)
