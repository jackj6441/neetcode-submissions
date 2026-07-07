class Solution:
    def jump(self, nums: List[int]) -> int:
        m = {}
        def dfs(i):
            if i in m:
                return m[i]
            if i == len(nums)-1:
                return 0
            if nums[i] == 0:
                return float('inf')
            
            end = min(len(nums), i+nums[i]+1)
            res = float('inf')
            for j in range(i+1,end):
                res = min(res, 1+dfs(j))
            m[i] = res
            return res
        return dfs(0)
                
                