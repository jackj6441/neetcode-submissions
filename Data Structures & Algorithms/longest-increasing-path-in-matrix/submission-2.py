class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        h,w = len(matrix),len(matrix[0])
        m  = {}
        def dfs(i,j,pre):
            if not (0 <= i < h) or not (0 <= j < w) or matrix[i][j] <= pre:
                return 0
            if (i,j,pre) in m:
                return m[(i,j,pre)]
            # print(i,j, matrix[i][j],pre)
            if matrix[i][j] > pre:
                res = 1 + max(dfs(i+1,j,matrix[i][j]),
                dfs(i-1,j,matrix[i][j]),
                dfs(i,j+1,matrix[i][j]),
                dfs(i,j-1,matrix[i][j]))
                m[(i,j,pre)] = res
                return res
            else:
                m[(i,j,pre)] = 0
                return 0
        res = 0
        for i in range(h):
            for j in range(w):
                compare = dfs(i,j,-1)
                # print(i,j,compare)
                res = max(res,compare )
        return res