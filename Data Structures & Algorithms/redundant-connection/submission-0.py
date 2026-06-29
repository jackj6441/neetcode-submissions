class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            p1 = find(i)
            p2 = find(j)
            print(parent)
            if p1 == p2:
                return False
            parent[p1] = p2
            return True
        for i, j in edges:
            if not union(i,j):
                return [i, j]
        return None