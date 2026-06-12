class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.cur = []
        self.curSum = 0
        i = 0
        def dfs(i):
            if i >= len(nums):
                return
            elif self.curSum > target:
                return
            elif self.curSum == target:
                res.append(self.cur.copy())
                return
            self.curSum += nums[i]
            self.cur.append(nums[i])
            dfs(i)

            self.curSum -= nums[i]
            self.cur.remove(nums[i])
            dfs(i+1)
        dfs(0)
        return res