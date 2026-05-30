class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        sign = ['+','-','*','/']
        tmp = 0
        for t in tokens:
            if t in sign and len(s) >= 2:
                t1 = int(s.pop())
                t2 = int(s.pop())
                if t == '+':
                    tmp = t1 + t2
                elif t == '*':
                    tmp = t1*t2
                elif t == '-':
                    tmp = t2-t1
                elif t == '/':
                    tmp = int(t2/t1)
                s.append(tmp)
            else:
                s.append(int(t))
            print(s)
        return s[0]
                