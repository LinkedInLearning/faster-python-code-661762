"""Example using cProfile"""
from login import login
from random import random


def gen_cases(n):
    """Generate tests cases"""
    for i in range(n):
        if random() > 0.1:  # 90% of logins are OK
            yield ('daffy', 'rabbit season')
        else:
            if random() < 0.2:
                yield ('tweety', 'puddy tat')  # no such user
            else:
                yield ('daffy', 'duck season')


def bench_login(cases):
    """Benchmark login with test cases"""
    for user, passwd in cases:
        login(user, passwd)


if __name__ == '__main__':
    n = 1000
    cases = list(gen_cases(n))

    if 0:
        bench_login(cases)

    if 0:
        import cProfile
        cProfile.run('bench_login(cases)')

    if 1:
        import cProfile
        cProfile.run('bench_login(cases)', filename='prof.out')