class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        i = 0
        candidates.sort()
        def dfs(start,rest):
            if rest == 0:
                res.append(cur.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > rest:
                    break
                rest -= candidates[i]
                cur.append(candidates[i])
                dfs(i+1, rest)
                rest += candidates[i]
                cur.pop()
            

                
        dfs(0,target)
        return res
