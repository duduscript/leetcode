class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(digits)):
            if digits[len(digits)-1-i] == 9:
                digits[len(digits)-1-i] = 0
            else:
                digits[len(digits)-1-i] += 1
                break
        return digits if digits[0] != 0 else [1]+digits