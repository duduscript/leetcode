class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [1]*n
        for i in xrange(m-1):
            for j in xrange(1,n):
                l[j] += l[j-1]
        return l[-1]