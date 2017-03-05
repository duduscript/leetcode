class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        elif num == 1:
            return True
        elif num%2 == 0:
            return self.isUgly(num/2)
        elif num%3 == 0:
            return self.isUgly(num/3)
        elif num%5 == 0:
            return self.isUgly(num/5)
        else:
            return False