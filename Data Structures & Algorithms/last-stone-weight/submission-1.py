class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        print(heap)
        while len(heap) > 1:
            y = - (heapq.heappop(heap))
            x = - (heapq.heappop(heap))
            cur = y - x
            if cur > 0:
                heapq.heappush(heap, -cur)
        return -heap[0] if len(heap) > 0 else 0

