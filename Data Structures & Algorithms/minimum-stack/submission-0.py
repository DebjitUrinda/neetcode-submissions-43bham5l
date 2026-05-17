class MinStack:

    def __init__(self):
        # Main stack stores all values.
        self.stack = []

        # min_stack[i] stores the minimum value among self.stack[0:i+1].
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack.
        self.stack.append(val)

        # Push the minimum so far onto min_stack.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # Pop from both stacks to keep them aligned.
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top element.
        return self.stack[-1]

    def getMin(self) -> int:
        # The current minimum is always on top of min_stack.
        return self.min_stack[-1]