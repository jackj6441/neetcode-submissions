class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def helper(l, r):
            res = 0
            # if l < 0 or r >= n:
            #     return False
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    res += 1
                    l-=1
                    r+=1
                else:
                    return res
            return res
        res = 0
        for i in range(n):
            l, r = i, i
            res += helper(l, r)
            l, r = i, i+1
            res += helper(l, r)
        return res