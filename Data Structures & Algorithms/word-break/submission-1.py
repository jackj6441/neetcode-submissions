
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        se = set(wordDict)
        maxL = 0
        for w in wordDict:
            maxL = max(maxL, len(w))
        memo = {}
        def dfs(i):
            
            if i in memo:
                return memo[i]
            if i == len(s):
                memo[i] = True
                return True
            print(i)
            for j in range(i, min(len(s), i + maxL)):
                print(i, j, s[i:j+1])
                if s[i:j+1] in se:
                    
                    if dfs(j+1):
                        return True
            memo[i] = False
            return False
        return dfs(0)
            