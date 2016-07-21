class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1,1]
        for i in xrange(2,n+1):
            a.append(sum([a[j]*a[i-j-1] for j in xrange(i)]))
        return a[-1]