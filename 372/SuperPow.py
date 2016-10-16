class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b,r,tmp = int(''.join(map(str,b))),1,a%1337
        while b:
            if b & 1:
                r *= tmp
                r %= 1337
            b >>= 1
            tmp = (tmp*tmp)%1337
        return r