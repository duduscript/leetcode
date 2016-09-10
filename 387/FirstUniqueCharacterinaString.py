class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
            dic[c] = 1 if c not in dic else dic[c]+1
        for i in xrange(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1