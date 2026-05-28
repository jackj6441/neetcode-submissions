class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        out = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == (nums[i-1]+1):
                count +=1
            elif nums[i] == nums[i-1]:
                continue
            else:
                count = 1
            out = max(out, count)
        return out