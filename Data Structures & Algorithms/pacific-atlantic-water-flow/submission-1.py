class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()
        h, w = len(heights),len(heights[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        visit = [[False]*w for _ in range(h)]
        def bfs(q, track):
            while q:
                for _ in range(len(q)):
                    
                    i, j = q.popleft()
                    track.add((i,j))
                    for dx, dy in dirs:
                        if i+dx < 0 or i+dx >= h or j+dy < 0 or j+dy >= w:
                            continue
                        if visit[i+dx][j+dy] == False and heights[i+dx][j+dy] >= heights[i][j]:
                            q.append((i+dx,j+dy))
                            visit[i+dx][j+dy] = True
        q = deque()
        for i in range(h):
            q.append((i,0))
            visit[i][0] = True
        for j in range(w):
            q.append((0,j))
            visit[0][j] = True
        bfs(q, pac)
        q = deque()
        visit = [[False]*w for _ in range(h)]
        for i in range(h):
            q.append((i,w-1))
            visit[i][w-1] = True
        for j in range(w):
            q.append((h-1,j))
            visit[h-1][j] = True
        bfs(q, atl)
        common = list(set(pac) & set(atl))
        return common