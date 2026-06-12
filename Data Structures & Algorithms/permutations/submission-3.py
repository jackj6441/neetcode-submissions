class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, nums):
            if i == len(nums):
                self.res.append(nums.copy())
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1, nums)
                nums[i], nums[j] = nums[j], nums[i]
        self.res = []
        dfs(0, nums)
        return self.res

        
        