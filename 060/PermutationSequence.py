import math
class Solution(object):
    def getPermutationIn(self, n, k, l):
        if n == 1:return str(l[0])
        s = l[k/math.factorial(n-1)]
        l.remove(s)
        return str(s)+self.getPermutationIn(n-1,k%math.factorial(n-1),l)
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.getPermutationIn(n,k-1,range(1,n+1))