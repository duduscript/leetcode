class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for c in t:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        for c in s:
            dic[c] -= 1
        for c in dic:
            if dic[c] == 1:
                return c