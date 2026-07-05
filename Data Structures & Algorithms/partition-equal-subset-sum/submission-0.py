class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = 0
        for n in nums:
            s += n
        m = []
        def dfs(i, l, s):

            if l == s:
                return True
            if i >= len(nums):
                return False
            res = dfs(i+1, l+nums[i], s-nums[i])

            return res or dfs(i+1, l, s)
        
        return dfs(0, 0, s)
        