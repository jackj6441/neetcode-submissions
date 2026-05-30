class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        t = temperatures
        out = [0]*len(t)
        for i in range(len(t)):
            for j in range(i, len(t)):
                if t[j] > t[i]:
                    out[i] = (j-i)
                    break
        return out