class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:return True
        return False if n%2 == 1 or n <= 0 else self.isPowerOfTwo(n/2)