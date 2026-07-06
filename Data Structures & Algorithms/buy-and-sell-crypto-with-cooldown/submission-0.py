class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = {}
        def dfs(i, BorS, cooldown):
            if i >= len(prices):
                return 0
            if (i,BorS,cooldown) in m:
                return m[(i,BorS,cooldown)]
            if cooldown:
                return dfs(i+1, 'B', False)
            if BorS == 'B':
                res = max(-prices[i]+dfs(i+1,'S',False), dfs(i+1, 'B', False))
                m[(i,BorS,cooldown)] = res
                return res
            else:
                res = max(prices[i]+dfs(i+1,'B',True), dfs(i+1, 'S', False))
                m[(i,BorS,cooldown)] = res
                return res
        return dfs(0,'B',False)

                