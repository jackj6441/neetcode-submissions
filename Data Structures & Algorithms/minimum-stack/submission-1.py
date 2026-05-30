class MinStack:

    def __init__(self):
        self.s = []
        self.minS = [float('inf')]

    def push(self, val: int) -> None:
        self.s.append(val)
        if val < self.minS[-1]:
            self.minS.append(val)
        else:
            self.minS.append(self.minS[-1])

    def pop(self) -> None:
        tmp = self.s[-1]
        self.s.pop()
        self.minS.pop()
        return tmp

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minS[-1]