class Solution(object):
    def dfs(self,paths,path,s,l):
        if l == 0:
            paths.append(path)
        else:
            for i in xrange(len(s)):
                if i != 0 and s[i] == s[i-1]:
                    continue
                self.dfs(paths,path+[s[i]],s[i+1:],l-1)
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        paths = []
        for i in xrange(len(nums)+1):
            self.dfs(paths,[],sorted(nums),i)
        return paths