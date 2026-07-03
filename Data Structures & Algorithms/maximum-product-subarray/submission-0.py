class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = {}
        res = nums[0]
        curMax = 1
        curMin = 1
        for i in range(len(nums)):
            print(res, curMax, curMin)
            cur = nums[i]
            tmp = curMax*cur
            curMax = max(cur, cur*curMax, cur*curMin)
            curMin = min(tmp, cur, cur*curMin)
            res = max(res, curMax)
        return res
