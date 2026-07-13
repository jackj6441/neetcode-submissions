class Solution:
    def isHappy(self, n: int) -> bool:
        def getNum(n):
            digits = [int(d) for d in str(n)]
            res = 0
            for d in digits:
                res += d**2
            # print(n, res)
            return res
        m = {}
        def dfs(n):
            # print(n)
            if n in m:
                return False
            num = getNum(n)
            if num == 1:
                return True
            else:
                m[n] = True
                return dfs(num)

        return dfs(n)