class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q = []
        intervals.sort()
        query = []
        for i in range(len(queries)):
            query.append([queries[i],i])
        query.sort()
        res = [-1] * len(query)
        for i in intervals:
            heapq.heappush(q, i)
        # print(query)
        inter_idx = 0
        int_q = []
        for val, idx in query:
            while inter_idx < len(intervals) and val >= intervals[inter_idx][0]:
                start, end = intervals[inter_idx]
                time = end - start + 1
                heapq.heappush(int_q, (time, end))
                inter_idx += 1
            # print(val, idx, int_q, res)
            while int_q and int_q[0][1] < val:
                heapq.heappop(int_q)
            if int_q:
                time = int_q[0][0]
                res[idx] = time
            
        return res