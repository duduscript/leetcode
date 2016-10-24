class Solution(object):
    def isPalindrome(self, s):
        return s == s[::-1]
    def dfs(self, s,path ,paths):
        if len(s) == 0:
            paths.append(path)
        for i in xrange(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.dfs(s[i+1:],path+[s[:i+1]],paths)
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        paths = []
        self.dfs(s, [], paths)
        return paths
