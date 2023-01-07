#!/usr/bin/env python3
"""Basic type-annotated function"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum mixed list function"""
    return sum(mxd_lst)
