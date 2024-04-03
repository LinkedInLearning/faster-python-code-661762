"""memory_profiler example"""


def sum_of_diffs(vals):
    """Compute sum of diffs"""
    vals2 = vals[1:]

    total = 0
    for v1, v2 in zip(vals, vals2):
        total += v2 - v1

    return total


if __name__ == '__main__':
    vals = list(range(1, 1_000_000, 3))
    print(sum_of_diffs(vals))
