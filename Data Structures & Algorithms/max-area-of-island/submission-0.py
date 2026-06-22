class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        h, w = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= h or j < 0 or j >= w:
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs (i+1, j) + dfs (i, j+1)+ dfs(i-1, j)+dfs(i,j-1)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res