class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        cur = ""
        def dfs(s):
            nonlocal cur
            if s >= len(digits):
                res.append(cur)
                return
            for i in range(0, len(m[digits[s]])):
                cur = cur + m[digits[s]][i]
                dfs(s+1)
                cur = cur[:-1]
        dfs(0)
        return res
