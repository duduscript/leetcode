# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left,right = [],[]
        for iv in intervals:
            if iv.end < newInterval.start:
                left.append(iv)
            elif iv.start > newInterval.end:
                right.append(iv)
            else:
                if iv.start < newInterval.start:
                    newInterval.start = iv.start
                if iv.end > newInterval.end:
                    newInterval.end = iv.end
        return left + [newInterval] + right