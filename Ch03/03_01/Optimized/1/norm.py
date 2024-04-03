"""Name caching"""

class config:
    """Global configuration"""
    factor = 7.3
    threshold = 12


def normalize(numbers):
    """Normalize list of numbers"""
    norm = []
    for num in numbers:
        if num > config.threshold:
            num /= config.factor
        norm.append(num)
    return norm

def normalize2(numbers):
    """Normalize list of numbers, caching names"""
    thr = config.threshold
    fact = config.factor

    norm = []
    for num in numbers:
        if num > thr:
            num /= fact
        norm.append(num)
    return norm

if __name__ == '__main__':
    import random

    random.seed(353)
    numbers = [random.randint(5, 50) for _ in range(1000)]
