class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = 0
        for n in nums:
            s += n
        m = [False] * len(nums)
        def dfs(i, l, s):

            if l == s:
                return True
            if i >= len(nums):
                return False
            res1 = dfs(i+1, l+nums[i], s-nums[i]) or dfs(i+1, l, s)
            m[i] = res1
            return res1
        
        return dfs(0, 0, s)
        