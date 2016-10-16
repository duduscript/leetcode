class Solution(object):
    paths = 0
    def dfs(self,path,sub,add,n):
        if len(path) == n:
            self.paths += 1
            return
        for i in xrange(n):
            if i+len(path) in add or i-len(path) in sub or i in path:
                continue
            else:
                self.dfs(path+[i],sub | set([i-len(path)]),add | set([i+len(path)]),n)
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dfs([],set(),set(),n)
        return self.paths