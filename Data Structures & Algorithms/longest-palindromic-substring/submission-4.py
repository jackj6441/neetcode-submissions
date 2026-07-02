class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def helper(s, l, r):
            # print(s, l, r)
            while r < len(s) and l >= 0 and s[l] == s[r]:
                l -= 1
                r += 1
            return (l+1, r-1)
        track = float('-inf')
        res = ''
        for i in range(n):
            
            l1, r1 = helper(s, i, i)
            print(l1, r1, track)
            if r1 - l1 > track:
                res = s[l1:r1+1]
                track = r1 - l1
            l2, r2 = helper(s, i, i+1)
            print(l2, r2, track)
            if r2 - l2 > track:
                res = s[l2:r2+1]
                track = r2 - l2
        return res

            
        
            