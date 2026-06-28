class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = []
        m = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            m[i].append(j)
        print(m)
        visit = {i: 0 for i in range(numCourses)}
        def dfs(c):
            if visit[c] == 1:
                return False
            if visit[c] == 2:
                return True
            visit[c] = 1
            for tmp in m[c]:
                if not dfs(tmp):
                    return False
            out.append(c)
            visit[c] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return out