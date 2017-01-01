class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:return 0
        isprime,upper = [True] * n, int(pow(n,0.5))+1
        isprime[:2] = [False]*2
        for i in xrange(2,upper):
            if isprime[i]:
                isprime[i*i::i] = [False]*len(isprime[i*i::i])
        return len(filter(lambda x:x,isprime))