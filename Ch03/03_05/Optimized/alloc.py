"""Fixed list allocation"""


def allocz(size):
    """Alloc zeros with range"""
    return [0 for _ in range(size)]


def allocz_fixed(size):
    """Alloc zeros with *"""
    return [0] * size
