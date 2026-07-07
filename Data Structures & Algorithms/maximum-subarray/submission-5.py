class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = {}
        def dfs(i, flag):
            if i >= len(nums):
                if flag == 1 or flag == 2:
                    return 0
                return float('-inf')
            if (i,flag) in m:
                return m[(i,flag)]
            if flag == 1:
                res = nums[i] + max(dfs(i+1,1), dfs(i+1,2))
            elif flag == 0:
                res = max(nums[i]+max(dfs(i+1, 1),0), dfs(i+1,0))
            else:
                res = 0
            # print(i,res)
            m[(i,flag)] = res
            return res
        return dfs(0,0) 