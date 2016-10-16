class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag,num = 0,0
        if x < 0:
            flag = 1
            x = -x
        while x:
            num *= 10
            num += x%10
            x /=10
        if flag:
            num = -num
        if num > 2**31-1 or num <- 2**31:
            num = 0
        return num