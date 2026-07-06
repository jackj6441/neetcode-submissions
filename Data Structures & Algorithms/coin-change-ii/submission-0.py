class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = {}
        def dfs(i,left):
            if i >= len(coins) or left < 0:
                return 0
            if (i,left) in m:
                return m[(i,left)]
            if left == 0:
                return 1
            res = dfs(i,left-coins[i]) + dfs(i+1,left)
            m[(i,left)] = res
            return res
        return dfs(0,amount)