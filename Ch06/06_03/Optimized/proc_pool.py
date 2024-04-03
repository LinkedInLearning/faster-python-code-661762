"""Process pool example"""
from concurrent.futures import ProcessPoolExecutor
import bz2


def unpack(requests):
    """Unpack a list of requests compressed in bz2"""
    return [bz2.decompress(request) for request in requests]


def unpack_proc(requests):
    """Unpack a list of requests compressed in bz2 using a process pool"""
    # Default to numbers of cores
    with ProcessPoolExecutor() as pool:
        return list(pool.map(bz2.decompress, requests))


if __name__ == '__main__':
    with open('huck-finn.txt', 'rb') as fp:
        data = fp.read()

    bz2data = bz2.compress(data)
    print(len(bz2data) / len(data))  # About 27%
    print(bz2.decompress(bz2data) == data)  # Loseless

    requests = [bz2data] * 300
