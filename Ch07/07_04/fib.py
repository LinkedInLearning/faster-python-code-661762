"""Fibonacci"""


def fib(n):
    """Return the n'th fibonacci number"""
    a, b = 1, 1
    while n:
        a, b = b, a + b
        n -= 1
    return a
