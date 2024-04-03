"""Multiply vectors"""


def vmul(vec1, vec2):
    """Return element wise multiplication"""
    return [v1*v2 for v1, v2 in zip(vec1, vec2)]
