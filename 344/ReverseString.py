class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = '1'*(len(s)+1)
        for i in xrange(1,len(s)+1):
            r[i] = s[-i]
        return r[1:]