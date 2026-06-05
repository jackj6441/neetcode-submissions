class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if m.get(n, 0) != 0:
                return n
            m[n] = m.get(n, 0) + 1

        return None