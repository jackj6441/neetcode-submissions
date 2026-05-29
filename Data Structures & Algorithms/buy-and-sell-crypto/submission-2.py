class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        l,r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                out = max(out, profit)
            else:
                l = r
            r += 1
        return out