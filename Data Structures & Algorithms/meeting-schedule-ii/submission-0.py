"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        a = []
        for i in intervals:
            a.append([i.start, 'S'])
            a.append([i.end, 'E'])
        a.sort()
        res = 0
        count = 0
        print(a)
        for cur in a:
            if cur[1] == 'S':
                count += 1
            else:
                count -= 1
            res = max(res, count)
        return res

