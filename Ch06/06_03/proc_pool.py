"""Process pool example"""
import bz2


def unpack(requests):
    """Unpack a list of requests compressed in bz2"""
    return [bz2.decompress(request) for request in requests]


if __name__ == '__main__':
    with open('huck-finn.txt', 'rb') as fp:
        data = fp.read()

    bz2data = bz2.compress(data)
    print(len(bz2data) / len(data))  # About 27%
    print(bz2.decompress(bz2data) == data)  # Loseless

    requests = [bz2data] * 300
