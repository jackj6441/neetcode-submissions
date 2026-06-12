class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, 0, ans)
        return ans
    
    def dfs(self, nums: List[int], i: int, ans: List[List[int]]):
        if i == len(nums):
            ans.append(nums.copy())
        for j in range(i, len(nums)):
            self.swap(nums, i, j)
            self.dfs(nums, i + 1, ans)    
            self.swap(nums, i, j)    
        return None
        
    def swap(self, nums, i, j):
        tp = nums[i]
        nums[i] = nums[j]
        nums[j] = tp