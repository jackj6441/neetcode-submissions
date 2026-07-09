class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        limit = 0
        for i in range(len(intervals)-1):
            cur = intervals[i]
            limit = cur[1] if limit == 0 else limit
            nxt = intervals[i+1]
            print(limit, cur, nxt)
            if limit > nxt[0]:
                limit = min(cur[1],nxt[1],limit)
                res += 1
            else:
                limit = nxt[1]
        return res
