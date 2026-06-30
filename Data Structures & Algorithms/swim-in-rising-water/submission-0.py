class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        path = []
        q = []
        heapq.heappush(q, (grid[0][0],0,0))
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        h, w = len(grid), len(grid[0])
        visit = [[False] * w for _ in range(h)]
        while q:
            v, i, j  = heapq.heappop(q)
            visit[i][j] = True
            path.append(v)
            if i == h-1 and j == w-1:
                return max(path)
            
            for dx, dy in dirs:
                if i + dx < 0 or i + dx >= h or j + dy < 0 or j + dy >= w:
                    continue
                if visit[i+dx][j+dy]:
                    continue
                heapq.heappush(q, (grid[i+dx][j+dy],i+dx,j+dy))
        return -1

                
                
