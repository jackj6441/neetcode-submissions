class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = [False for _ in range(n)]
        dist = [float('inf') for  _ in range(n)]
        res = 0
        edge = 0
        node = 0
        while edge < n-1:
            visit[node] = True
            nxtNode = -1
            for i in range(n):
                if not visit[i]:
                    curDist = (abs(points[i][0] - points[node][0]) +
                           abs(points[i][1] - points[node][1]))
                    dist[i] = min(dist[i], curDist)
                    if nxtNode == -1 or dist[nxtNode] > dist[i]:
                        nxtNode = i
            print(node, nxtNode)
            res += dist[nxtNode]
            edge += 1
            node = nxtNode
        return res

                    