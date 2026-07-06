class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = {}
        def dfs(i,left):
            
            if i > len(nums):
                return 0
            if i == len(nums):
                if left == target:
                    return 1
                else:
                    return 0
            print(i,left)
            if (i,left) in m:
                return m[(i,left)]
            res = dfs(i+1, left+nums[i]) + dfs(i+1, left-nums[i])
            m[(i,left)] = res
            return res
        return dfs(0,0)