from fib import fib


def test_fib(benchmark):
    result = benchmark(fib, 30)
    assert result == 1346269
