class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i, l in enumerate(s):
            m[l] = i
        print(m)
        end, start = 0,0
        res = []
        for i, ch in enumerate(s):
            end = max(end, m[ch])

            if i == end:
                res.append(end-start+1)
                start = i+1
        
        return res