class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        m = {}
        def helper(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in m:
                return m[i]
            cur = s[i]
            out = 0
            if cur != '0':
                out += helper(i+1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                out += helper(i+2) 
                # print(i, s[i:i+2], out)
            m[i] =  out 
            return out 
        
        return helper(0)