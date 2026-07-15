class MinStack:

# last in first out

    def __init__(self):
        self.stack = [] # list
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return (self.stack[-1])
        

    def getMin(self) -> int:
        return self.minStack[-1]