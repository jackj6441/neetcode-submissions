class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        m = {i:[] for i in range(n)}
        for i, j in edges:
            m[i].append(j)
            m[j].append(i)
        # print(m)
        visit = {i:False for i in range(n)}
        def dfs(n):
            # print(n, visit)
            visit[n] = True
            for nei in m[n]:
                if not visit[nei]:
                    dfs(nei)
        for i in range(n):
            if not visit[i]:
                dfs(i)
                count += 1
        return count
        
            
            