class MinStack:

    def __init__(self):
        self.stack = []
        self.stackM = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackM:
            self.stackM.append(val)
        else:
            current_min = min(val, self.stackM[-1])
            self.stackM.append(current_min)
            
    def pop(self) -> None:
        self.stack.pop()
        self.stackM.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackM[-1]
