class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 = []
        s2 = []
        for i,ch in enumerate(s):
            
            if ch == '(':
                s1.append(i)
            elif ch == ')':
                if len(s1) <= 0:
                    if len(s2) <= 0:
                        return False
                    else:
                        s2.pop()
                else:
                    s1.pop()
            else:
                s2.append(i)
            print(s1,s2)
        if len(s1) > len(s2):
            return False
        while len(s1) > 0 and len(s2) > 0:
            cur1 = s1.pop()
            cur2 = s2.pop()
            print(cur1, cur2)
            if cur1 > cur2:
                return False
        return len(s1) == 0