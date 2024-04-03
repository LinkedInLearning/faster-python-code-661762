"""Small Math library"""


def sqrt(n, epsilon=0.0001):
    """Return square root of a number"""
    guess = 1.0

    while abs(guess*guess - n) > epsilon:
        guess = (n/guess + guess) / 2.0

    return guess
