"""Example on using joblib for caching"""

from joblib import Memory
from os.path import expanduser

from Levenshtein import distance as levenshtein

memory = Memory(expanduser('~/.cache/spell'), verbose=0)


@memory.cache
def load_words():
    with open('en-words.txt') as fp:
        return tuple(line.strip().lower() for line in fp)


@memory.cache
def spell(word, count=10, dict_words=None):
    dict_words = load_words() if dict_words is None else dict_words
    return sorted(dict_words, key=lambda dw: levenshtein(word, dw))[:count]


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='spell checker')
    parser.add_argument('word', help='word to check', nargs='?')
    parser.add_argument(
        '--count', type=int, default=10, help='number of words to return')
    parser.add_argument(
        '--clear-cache', help='clear cache', action='store_true',
        default=False)
    args = parser.parse_args()

    if args.clear_cache:
        memory.clear()
        raise SystemExit

    if not args.word:
        raise SystemExit('no word given')

    for word in spell(args.word, args.count):
        print(word)
