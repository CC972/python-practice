class Stack:
    """Simple implementation of a stack backed by a list"""

    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.size == 0:
            raise ValueError("Stack is empty")
        return self._stack.pop()

    @property
    def size(self):
        return len(self._stack)

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(str(self._stack))})"
