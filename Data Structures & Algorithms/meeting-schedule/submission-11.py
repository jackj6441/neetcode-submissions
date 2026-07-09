"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        a = []
        for I in intervals:
            a.append([I.start,I.end])
        a.sort()
        print(a)
        preS, preE = a[0][0], a[0][1]
        for i in range(1, len(a)):
            cur = a[i]
            if preE > cur[0]:
                return False
            preE = cur[1]
        return True
            