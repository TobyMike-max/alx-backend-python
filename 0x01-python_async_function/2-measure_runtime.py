#!/usr/bin/env python3
"""Measure the runtime"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function the measures runtime of an async function
    Args:
        n(int): Number of times to call function
        delay(int): Maximum time for delay
    Return:
        total_time / n(float)
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return total_time / n
