class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[]*n for i in range(n)]
        for a, b, c in flights:
            adj[a].append([c, b])
        step = 0
        def bfs(q):
            while q:
                for i in range(len(q)):
                    print(q)
                    cost, d, step = heapq.heappop(q)
                    
                    if step > k:
                        continue
                    print(cost, d, step)
                    if d == dst:
                        return cost
                    for price, dest in adj[d]:
                        heapq.heappush(q, (price+cost, dest, step+1))
            return -1
        q = []
        for price, d in adj[src]:
            heapq.heappush(q, (price, d, step))
        return bfs(q)
                    