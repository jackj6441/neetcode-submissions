class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)

    def pop(self) -> None:
        tmp = self.s[-1]
        self.s.pop()
        return tmp

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        out = float('inf')
        for i in self.s:
            out = min(out, i)
        return out