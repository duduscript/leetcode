class Solution(object):
    def dfs(self,paths,path,sub,add,n):
        if len(path) == n:
            paths.append(path)
        for i in xrange(n):
            if i+len(path) in add or i-len(path) in sub or i in path:
                continue
            else:
                self.dfs(paths,path+[i],sub | set([i-len(path)]),add | set([i+len(path)]),n)
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        paths = []
        self.dfs(paths,[],set(),set(),n)
        return [['.'*pos+'Q'+'.'*(n-pos-1) for pos in vec] for vec in paths]