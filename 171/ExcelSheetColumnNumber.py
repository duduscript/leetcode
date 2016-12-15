class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtn = 0
        for c in s:
            rtn *= 26
            rtn += ord(c)-64
        return rtn