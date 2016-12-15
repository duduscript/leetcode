class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(filter(lambda x:x == '1',bin(n)))