#!/usr/bin/env python3

'''
Calculate the total running time of wait_n caroutine
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    measure_time : Measure time of execution it took wait_n to execute
    Arguements:
        max_delay: The maximum time the funcion shoud sleep
        n : The number of caro rutines
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return ((time.perf_counter() - start) / n)
