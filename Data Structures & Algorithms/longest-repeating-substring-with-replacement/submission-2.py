class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 1
        out = 0
        m = {}
        most = 0
        for r in range(len(s)):
            m[s[r]]  = m.get(s[r],0) + 1
            most = max(most,m[s[r]])
            while (r-l+1) - most > k:
                m[s[l]] -= 1
                l+=1
            out = max(r-l+1, out)
            
        return out