"""Calculate grades - bisect example"""
from bisect import bisect

cutoffs = [60, 70, 80, 90]
names = 'FDCBA'

def grade(score):
    """Give a letter grade from numeric score

    >>> grade(80)
    'C'
    """
    for cutoff, name in zip(cutoffs, names):
        if score < cutoff:
            return name
    return 'A'

def grade2(score):
    """Give a letter grade from numeric score

    >>> grade(80)
    'C'
    """
    i = bisect(cutoffs, score)
    return names[i]

def test_grades(fn=grade):
    cases = [
        (100, 'A'),
        (92, 'A'),
        (87, 'B'),
        (76, 'C'),
        (62, 'D'),
        (60, 'D'),
        (0, 'F'),
    ]

    for score, expected in cases:
        assert fn(score) == expected


if __name__ == '__main__':
    test_grades()
    test_grades(fn=grade2)
