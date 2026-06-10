class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance (p2):
            x1,y1 = 0, 0
            x2,y2 = p2[0],p2[1]
            return (((x1 - x2)**2 + (y1 - y2)**2))
        heap = []

        for p in points:
            heapq.heappush(heap, (distance(p), p))
        print(heap)
        
        ans = []
        for i in range(k):
            cur = heapq.heappop(heap)
            ans.append(cur[1])
        return ans
        