class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ms,mt = {},{}
        for i in xrange(len(s)):
            if s[i] in ms and ms[s[i]] != t[i]:
                return False
            if t[i] in mt and mt[t[i]] != s[i]:
                return False
            ms[s[i]],mt[t[i]] = t[i],s[i]
        return True