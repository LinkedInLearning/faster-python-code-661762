"""Cachine fibonnaci"""


def fib(n):
    """Return nth fiboacci number"""
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


_fib_cache = {}


def fibc(n):
    """Return nth fiboacci number (cached)"""
    if n < 2:
        return 1

    val = _fib_cache.get(n)
    if val is None:
        _fib_cache[n] = val = fibc(n-1) + fibc(n-2)
    return val
