class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        def rob_linear(sub_nums: List[int]) -> int:
            k = len(sub_nums)
            if k == 1: return sub_nums[0]
            
            dp = [0] * k
            dp[0] = sub_nums[0]
            dp[1] = max(sub_nums[0], sub_nums[1])
            
            for i in range(2, k):
                dp[i] = max(dp[i-2] + sub_nums[i], dp[i-1])
                
            return dp[-1]
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))