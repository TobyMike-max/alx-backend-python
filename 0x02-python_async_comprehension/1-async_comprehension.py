#!/usr/bin/env python3
""" Async Comprehensions/coroutine"""
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """Function that returns a list"""
    Final = [y async for y in async_generator()]
    return Final
