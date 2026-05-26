class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if m.get(need, -1) >= 0:
                return [m[need],i]
            m[nums[i]] = i
            
        return None
            