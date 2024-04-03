"""Example on pre calculating"""


def nbits(val):
    """Return number of bits set to 1 in n"""
    n = 0

    while val:
        if val & 1:
            n += 1
        val >>= 1

    return n


def test_nbits(fn):
    cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (6, 2),
        (7, 3),
    ]
    for val, n in cases:
        assert fn(val) == n


num_bits = 16
max_val = int('1' * num_bits, 2)

_bit_cache = [nbits(n) for n in range(max_val + 1)]


def nbits_fixed(n):
    """Return number of bits set to 1 in n"""
    if n > max_val:
        raise ValueError(f'n too large: {n} > {max_val}')
    return _bit_cache[n]


if __name__ == '__main__':
    test_nbits(nbits)
    test_nbits(nbits_fixed)
