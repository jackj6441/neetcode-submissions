class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        h, w = len(grid),len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= h or j < 0 or j >= w:
                return 
            if grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs (i+1, j)
            dfs (i, j+1)
            dfs(i-1, j)
            dfs(i,j-1)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i, j)
        return count

