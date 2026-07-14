class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            mask = 1 << i

            if n & mask:
                res += 1

        return res