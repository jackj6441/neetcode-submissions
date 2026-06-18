class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(st):
            l, r = 0, len(st)-1
            while l <= r:
                if st[l] != st[r]:
                    return False
                l +=1
                r -= 1
            return True
        res = []
        cur = []
        i = 0
        def dfs(start):
            if start >= len(s):
                res.append(cur.copy())
                return 
            for i in range(start, len(s)):
                print(start, i, s[start:i+1])
                if isPali(s[start:i+1]):
                    cur.append(s[start:i+1])
                    dfs(i+1)
                    cur.pop()
            
        dfs(0)
        return res
