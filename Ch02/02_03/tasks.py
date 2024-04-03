"""Task queue - deque example"""

class TaskQueue:
    """Task queue using list"""
    def __init__(self):
        self._tasks = []

    def push(self, task):
        self._tasks.insert(0, task)

    def pop(self):
        return self._tasks.pop()

    def __len__(self):
        return len(self._tasks)


def test_queue(count=100):
    tq = TaskQueue()

    for i in range(count):
        tq.push(i)
        assert len(tq) == i + 1

    for i in range(count):
        assert tq.pop() == i
        assert len(tq) == count - i - 1


if __name__ == '__main__':
    test_queue()
  
