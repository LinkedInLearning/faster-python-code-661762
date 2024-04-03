"""A timed metric decorator"""
from functools import wraps
from time import monotonic


def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kw):
        start = monotonic()
        try:
            return fn(*args, **kw)
        finally:
            duration = monotonic() - start
            # Save to database
            print('{} took {:.3f}sec'.format(fn.__name__, duration))

    return wrapper


if __name__ == '__main__':
    # Usage example
    from time import sleep

    @timed
    def add(a, b):
        sleep(a/10)  # Simulate work
        return a + b
