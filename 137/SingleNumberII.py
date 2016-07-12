class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b,ta = 0,0,0
        for x in nums:
            ta,b = a&~b&~x | ~a&b&x,~a&b&~x | ~a&~b&x
            a = ta
        return a|b