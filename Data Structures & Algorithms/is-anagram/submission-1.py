class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for n in s:
            m[n] = m.get(n,0)+1
        for c in t:
            if m.get(c,0) == 0 or m[c] < 0:
                return False
            else:
                m[c] -= 1
        for c in m:
            if m[c] != 0:
                return False
        return True