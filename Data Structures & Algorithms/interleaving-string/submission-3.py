class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(i,j,k):
            if k >= len(s3):
                return True
            if i < len(s1) and j >= len(s2):
                return dfs(i+1,j,k+1) if s3[k] == s1[i] else False
            elif i >= len(s1) and j < len(s2):
                return dfs(i,j+1,k+1) if s3[k] == s2[j] else False
            if (i,j,k) in m:
                return m[(i,j,k)]
            l1 = s1[i]
            l2 = s2[j]
            l3 = s3[k]
            res1 = False
            res2 = False
            if l3 == l1:
                res1 = dfs(i+1,j,k+1)
            if l3 == l2:
                res2 = dfs(i,j+1,k+1)
            res = res1 or res2
            m[(i,j,k)] = res
            return res
        return dfs(0,0,0)
            