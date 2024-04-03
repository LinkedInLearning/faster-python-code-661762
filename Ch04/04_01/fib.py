"""Cachine fibonnaci"""


def fib(n):
    """Return nth fiboacci number"""
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)



