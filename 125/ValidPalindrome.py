class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x for x in list(s.lower()) if (x.isalpha() or x.isdigit())]
        for i in xrange(len(s)/2):
            if s[i].lower() != s[len(s) - 1 - i].lower():
                return False
        return True