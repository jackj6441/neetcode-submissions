class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        ct = -1
        out = []
        for i in range(len(nums)):
            if nums[i] == 0:
                if ct >= 0:
                    return [0]*len(nums)
                ct = i
            else:
                mul = mul*nums[i]
        if ct >= 0:
            return [0]*ct + [mul] + [0]*(len(nums)-ct-1)
        for i in range(len(nums)):
            out.append(mul//nums[i])

        return out
            