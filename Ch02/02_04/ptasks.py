"""Priority task queue - heap example"""

from random import random, seed, randint


class PriorityQueue:
    """Priority queue using list + sort"""
    def __init__(self):
        self._tasks = []

    def push(self, task, priority):
        self._tasks.append((priority, task))
        self._tasks.sort(reverse=True)

    def pop(self):
        return self._tasks.pop()[1]

    def __len__(self):
        return len(self._tasks)


def test_pqueue(cls=PriorityQueue):
    pq = cls()

    todo = [
        (2, 'fix bug'),
        (10, 'read email'),
        (4, 'add feature'),
        (6, 'eat lunch'),
    ]

    for priority, task in todo:
        pq.push(task, priority)

    tasks = []
    tasks.append(pq.pop())
    tasks.append(pq.pop())

    # Don't forget to nap
    pq.push('nap', 5)

    while pq:
        tasks.append(pq.pop())

    expected = [item[1] for item in sorted(todo + [(5, 'nap')])]
    assert tasks == expected


def gen_cases(count):
    seed(353)  # Same cases every time

    cases = []
    for i in range(count):
        if random() < 0.5:
            cases.append(-1)
        else:
            cases.append(randint(1, 100))
    return cases


def benchmark_pq(cases):
    pq = PriorityQueue()

    for i, case in enumerate(cases):
        if case < 0 and pq:
            pq.pop()
        elif case > 0:
            pq.push(f'task {i}', case)


if __name__ == '__main__':
    test_pqueue()
    
