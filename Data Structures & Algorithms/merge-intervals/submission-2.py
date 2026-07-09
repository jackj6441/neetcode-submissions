class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        pre = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            cur = intervals[i]
            # print(pre,cur)
            if pre[1] < cur[0]:
                res.append(pre)
                pre = cur
            else:
                pre = [min(pre[0],cur[0]), max(pre[1],cur[1])]
        res.append(pre)
        return res
