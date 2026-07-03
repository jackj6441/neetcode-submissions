class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        m = {}
        def dfs(left, i):
            if (left, i) in m:
                return m[(left, i)]
            if left < 0:
                return float('inf')
            if left == 0:
                return 0
            if i >= n:
                return float('inf')
            res = min(1+ dfs(left-coins[i], i),dfs(left, i+1))
            m[(left, i)] = res
            return res
        res = dfs(amount, 0)
        return -1 if res == float('inf') else res

            