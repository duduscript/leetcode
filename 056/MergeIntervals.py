# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals,cmp=lambda x,y:cmp(x.start,y.start))
        foo,bar = [],intervals[0]
        for x in intervals:
            if x.start <= bar.end <x.end:
                bar.end = x.end
            elif x.start > bar.end:
                foo.append(bar)
                bar = x
        foo.append(bar)
        return foo