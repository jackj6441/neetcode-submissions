class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        
        for i in range(len(nums)-k+1):
            count = 0
            tmp = nums[i]
            for j in range(i, i + k):
                tmp = max(tmp, nums[j])
            out.append(tmp)
        return out
