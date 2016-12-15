import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        rtn,fact = 0,5
        while fact <= n:
            rtn += n/fact
            fact *= 5
        return rtn