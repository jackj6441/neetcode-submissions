import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for n in nums:
            self.add(n)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif len(self.heap) >= self.k and self.heap[0] <= val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        print(self.heap)
        return self.heap[0]
        
