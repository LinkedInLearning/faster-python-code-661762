"""Small Math library - in Cython"""


def sqrt(double n, double epsilon=0.0001):
    """Return square root of n"""
    cdef double guess = 1.0

    while abs(guess*guess - n) > epsilon:
        guess = (n/guess + guess) / 2.0

    return guess

