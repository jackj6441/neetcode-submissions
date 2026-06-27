class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i:[] for i in range(numCourses)}
        for i, j in prerequisites:
            m[j].append(i)
        print(m)
        visiting = set()
        def dfs(c):
            if c in visiting:
                return False
            if m[c] == []:
                return True
            visiting.add(c)
            for req in m[c]:
                if not dfs(req):
                    return False
            visiting.remove(c)
            m[c] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            