"""Example on pre calculating"""


def nbits(val):
    """Return number of bits set to 1 in n"""
    n = 0

    while val:
        if val & 1:
            n += 1
        val >>= 1

    return n


def test_nbits():
    cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (6, 2),
        (7, 3),
    ]
    for val, n in cases:
        assert nbits(val) == n

if __name__ == '__main__':
    test_nbits()
   
