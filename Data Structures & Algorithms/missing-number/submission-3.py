class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c = []
        for i in range(len(nums)+1):
            c.append(i)
        print(c)
        for i in c:
            if i not in nums:
                return i
        return 0