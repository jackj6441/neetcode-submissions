class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        o = {}
        for hi in t:
            o[hi] = o.get(hi,0)+1
        res, resLen = [-1, -1], float("infinity")
        l = 0
        tmp = {}
        have, need = 0, len(o)
        for r in range(len(s)):
            c = s[r]
            tmp[c] = tmp.get(c,0) + 1
            if c in o and tmp[c] == o.get(c,0):
                have += 1
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l,r]
                tmp[s[l]] -= 1
                if s[l] in o and tmp[s[l]] < o[s[l]]:
                    have -= 1
                l += 1
            
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
