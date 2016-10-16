class Solution(object):
    def dfs(self,paths,path,s):
        if len(s) == 0:
            paths.append(path)
        else:
            for i in xrange(len(s)):
                if i != 0 and s[i] == s[i-1]:
                    continue
                self.dfs(paths,path+[s[i]],s[:i]+s[i+1:])
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        paths = []
        self.dfs(paths,[],sorted(nums))
        return paths