"""Optimizing function calls"""


def abs_even(num):
    """Make even number absolute in value

    >>> abs_even(-4)
    4
    >>> abs_event(-7)
    -7
    """
    if num % 2 == 0 and num < 0:
        return -num
    return num


def fix_nums(nums):
    """Fix numbers with abs_even"""
    return [abs_even(num) for num in nums]


if __name__ == '__main__':
    import random

    random.seed(353)
    # Test numbers
    numbers = [random.randint(-20, 20) for _ in range(1000)]
