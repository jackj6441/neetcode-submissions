class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        o = {}
        for hi in t:
            o[hi] = o.get(hi,0)+1
        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            tmp = {}
            for j in range(i, len(s)):
                tmp[s[j]] = tmp.get(s[j],0) + 1
                flag = True
                for t in o:
                    if o[t] > tmp.get(t, 0):
                        flag = False
                        break
                if flag and resLen > j - i + 1:
                    resLen = j - i + 1
                    res = [i,j]
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
