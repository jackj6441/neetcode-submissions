class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        step = -1
        q = deque()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        h,w = len(grid),len(grid[0])
        visit = [[False]*w for _ in range(h)]
        count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visit[i][j] = True
                if grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                
                if grid[i][j] == 0:
                    continue
                
                for dx, dy in dirs:
                    if i+dx < 0 or i+dx>= h or j+dy < 0 or j+dy >= w:
                        continue
                    if grid[i+dx][j+dy] == 1 and visit[i+dx][j+dy] == False:
                        q.append((i+dx, j+dy))
                        visit[i+dx][j+dy] = True
                        count -= 1
            
            step += 1
        return step if count == 0 else -1

            