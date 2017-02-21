class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        ans,table = 0,map(lambda x:pow(2,x),xrange(32))[::-1]
        for i in xrange(len(table)):
            if m < table[i] <= n:
                return 0
        for i in table:
            if m & i:
                ans = i
                m,n = m-i,n-i
                break
        return ans+self.rangeBitwiseAnd(m,n)