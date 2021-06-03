class Queue:
    """Simple implementation of a queue backed by a list"""

    def __init__(self):
        # Make attribute private (also to avoid shadowing queue method)
        self._queue = []

    def queue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if self.size == 0:
            raise ValueError("Queue is empty")
        return self._queue.pop(0)

    @property
    def size(self):
        return len(self._queue)

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(str(self._queue))})"
