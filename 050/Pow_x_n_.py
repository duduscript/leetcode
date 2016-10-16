class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = 1 if n >= 0 else 0
        tmp,rtn,n = x,1,abs(n)
        while n != 0:
            rtn = rtn*tmp if n&1 == 1 else rtn
            n,tmp = n/2,tmp*tmp
        return rtn if flag == 1 else 1/rtn