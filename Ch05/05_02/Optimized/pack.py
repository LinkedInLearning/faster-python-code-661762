"""Bin packing approximation example"""


def bin_pack(items, bin_size, bins=None):
    """Pack items in bins with size bin_size"""
    bins = [] if bins is None else bins

    if not items:
        return bins

    item = items[0]
    solutions = []
    for i, bin in enumerate(bins):
        if sum(bin) + item > bin_size:  # Can't add to bin
            continue
        sbins = bins[:]
        sbins[i].append(item)  # Add item to bin
        solutions.append(bin_pack(items[1:], bin_size, sbins))

    # Open new bin
    solutions.append(bin_pack(items[1:], bin_size, bins + [[item]]))

    return min(solutions, key=len)


def greedy_bin_pack(items, bin_size):
    """Pack items in bins with size bin_size - greedy first-fit"""
    bins = []

    for item in items:
        for bin in bins:
            if sum(bin) + item < bin_size:
                bin.append(item)
                break
        else:  # No fitting bin
            bins.append([item])
    return bins
