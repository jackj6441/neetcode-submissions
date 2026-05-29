class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = 0
        for i in range(len(s)):
            a = set()
            for j in range(i, len(s)):
                if s[j] in a:
                    break
                a.add(s[j])
            out = max(out, len(a))
        return out

        