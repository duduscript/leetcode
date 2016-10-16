class Solution(object):
    def dfs(self,paths,path,s):
        if len(s) == 0:
            paths.append(path)
        else:
            for i in xrange(len(s)):
                self.dfs(paths,path+[s[i]],s[:i]+s[i+1:])
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        paths = []
        self.dfs(paths,[],nums)
        return paths