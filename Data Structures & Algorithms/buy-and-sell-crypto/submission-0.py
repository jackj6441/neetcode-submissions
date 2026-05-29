class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                out = max(out, prices[j]-prices[i])
        return out