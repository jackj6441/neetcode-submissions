class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = {i:[] for i in range(n)}
        for i , j in edges:
            m[j].append(i)
            m[i].append(j)
        print(m)
        visit = set()
        def dfs(n,parent):
            visit.add(n)
            for node in m[n]:
                if node not in visit:
                    if not dfs(node, n):
                        return False
                elif node != parent:
                    return False
            return True
        if not dfs(0, -1):
            return False
        return True if len(visit) == n else False