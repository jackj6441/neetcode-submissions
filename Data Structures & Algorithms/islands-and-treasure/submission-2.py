class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        w,h = len(grid[0]), len(grid)
        INF = 2147483647
        visit = [[False for _ in range(w)]  for _ in range(h)]
        tres = deque()
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    tres.append((i,j))
        step = 0
        while tres:
            for _ in range(len(tres)):
                i, j = tres.popleft()
                
                if i < 0 or i >= h or j < 0 or j >= w:
                    continue
                if visit[i][j] or grid[i][j] == -1:
                    continue
                print(grid[i][j],i,j)
                visit[i][j] = True
                grid[i][j] = step
                tres.append((i+1, j))
                tres.append((i-1, j))
                tres.append((i, j+1))
                tres.append((i, j-1))
            step += 1
                
