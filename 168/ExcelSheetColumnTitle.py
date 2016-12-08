class Solution(object):
    def getchr(self, n):
        if n == 0:return ''
        return self.getchr((n-1)/26)+chr((n-1)%26+65)
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.getchr(n)