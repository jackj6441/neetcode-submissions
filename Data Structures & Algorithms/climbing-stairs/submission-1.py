class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        visit = {}
        def dp(rest):
            if rest in visit:
                return visit[rest]
            if rest == 0:
                return 1
            if rest < 0:
                return 0
            visit[rest] = dp(rest-1) + dp(rest-2)
            return visit[rest]
        return dp(n)