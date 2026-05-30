class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        t = temperatures
        out = [0]*len(t)
        s = []
        for i in range(len(t)):
            while len(s) > 0 and s[-1][0] < t[i]:
                out[s[-1][1]] = i - s[-1][1]
                s.pop()
            s.append([t[i],i])
        return out