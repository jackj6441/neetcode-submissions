class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        o = {}
        for s in s1:
            o[s] = o.get(s,0)+1
        check = {}
        l = 0
        for r in range(len(s2)):
            check[s2[r]]  = check.get(s2[r],0) + 1
            while r - l + 1 > len(s1):
                check[s2[l]] -= 1
                if check[s2[l]] == 0:
                    del check[s2[l]]
                l += 1
            if check == o:
                return True
        return False
