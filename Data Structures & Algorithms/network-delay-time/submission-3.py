class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for i in times:
            adj[i[0]-1].append([i[2], i[1]])
        print(adj)
        q = []
        visit = set()
        for i in range(len(adj[k-1])):
            heapq.heappush(q, adj[k-1][i])
        visit.add(k)
        t = 0
        while q:
            i, j = heapq.heappop(q)
            print(q, visit, t, j)
            if j in visit:
                continue
            visit.add(j)
            t = i
            for t1, t2 in adj[j-1]:
                if t2 in visit:
                    continue
                heapq.heappush(q, [t1+i,t2])
        return t if len(visit) == n else -1