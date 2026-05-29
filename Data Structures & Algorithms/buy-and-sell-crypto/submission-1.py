class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        min_price = prices[0]
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                out = max(out, p - min_price)

        return out