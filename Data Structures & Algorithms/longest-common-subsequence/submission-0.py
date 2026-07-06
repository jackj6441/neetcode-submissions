class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = {}
        l1,l2 = len(text1),len(text2)
        def dfs(i,j):
            if i >= l1 or j >= l2:
                return 0
            if (i,j) in m:
                return m[(i,j)]
            if text1[i] == text2[j]:
                res = max(1+dfs(i+1,j+1), dfs(i+1,j),dfs(i, j+1))
                m[(i,j)] = res
                return res
            else:
                res = max(dfs(i+1,j),dfs(i, j+1))
                m[(i,j)] = res
                return res
        return dfs(0,0)