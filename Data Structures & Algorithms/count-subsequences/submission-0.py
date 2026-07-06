class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = {}
        def dfs(i,j):
            if j >= len(t):
                return 1 
            if i >= len(s):
                return 0
            if (i,j) in m:
                return m[(i,j)]
            res = dfs(i+1,j)
            if s[i] == t[j]:
                res += dfs(i+1,j+1)
            print(i,j,s[i],t[j], res)
            m[(i,j)] = res
            return res
        return dfs(0,0)
            