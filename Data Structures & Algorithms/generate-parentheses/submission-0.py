class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(cur, l,r):
            
            if l == 0 and r == 0:
                res.append(cur)
                return
            if l > 0:
                helper(cur + '(', l-1, r)
            if r > l :
                helper(cur + ')', l, r-1)
        helper('', n,n)
        return res