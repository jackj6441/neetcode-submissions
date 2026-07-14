class CountSquares:

    def __init__(self):
        self.ptsCount = {}
        self.p = []

    def add(self, point: List[int]) -> None:
        x, y = point

        self.p.append((x, y))
        self.ptsCount[(x, y)] = self.ptsCount.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.p:
            if abs(px - x) != abs(py - y) or px == x:
                continue

            point1_count = self.ptsCount.get((x, py), 0)
            point2_count = self.ptsCount.get((px, y), 0)

            res += point1_count * point2_count
        return res
