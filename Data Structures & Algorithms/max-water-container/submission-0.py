class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                cur = min(heights[i],heights[j])*(j-i)
                out=max(cur,out)

        return out