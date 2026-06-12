class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, 0, ans)
        return ans
    
    def dfs(self, nums: List[int], i: int, ans: List[List[int]]):
        if i == len(nums):
            ans.append(nums.copy())
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.dfs(nums, i + 1, ans)    
            nums[i], nums[j] = nums[j], nums[i]
        return None