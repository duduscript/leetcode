class Solution(object):
    def generateMatrixFrom(self,rtn, m, n, k):
        if n == 0:
            return
        if n == 1:
            rtn[m][m] = k
            return
        for i in xrange(n-1):
            rtn[m][m+i] = k+i
        for i in xrange(n-1):
            rtn[m+i][m+n-1] = k+n-1+i
        for i in xrange(n-1):
            rtn[m+n-1][m+n-1-i] = k+2*(n-1)+i
        for i in xrange(n-1):
            rtn[m+n-1-i][m] = k+3*(n-1)+i
        self.generateMatrixFrom(rtn, m+1, n-2, k+4*(n-1))
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rtn = []
        for i in xrange(n):
            rtn.append([0]*n)
        self.generateMatrixFrom(rtn, 0, n, 1)
        return rtn