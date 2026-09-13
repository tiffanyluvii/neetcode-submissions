class MinStack:


    def __init__(self):
        self.stack = []
        self.minOrder = []

    def push(self, val: int) -> None:

        self.stack.append(val)
        minVal = min(val, self.minOrder[-1] if self.minOrder else val)
        self.minOrder.append(minVal)

    def pop(self) -> None:
        value = self.stack.pop()
        value = self.minOrder.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minOrder[-1]


        
