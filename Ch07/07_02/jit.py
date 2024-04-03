"""Example on using numba"""


def poly(coeffs, n):
    """Compute value of polynomial given coefficients"""
    total = 0
    for i, c in enumerate(coeffs):
        total += c * n**i
    return total


if __name__ == '__main__':
    coeffs = [4, 8, 15, 16, 23, 42]
