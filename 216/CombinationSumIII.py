class Solution(object):
    def dfs(self, k, n, rg, path, paths):
        if n == 0 and k == 0:
            paths.append(path)
        if len(rg) == 0 or rg[0] > n or k == 0 or n == 0:
            return
        self.dfs(k-1,n-rg[0],rg[1:],path+[rg[0]],paths)
        self.dfs(k,n,rg[1:],path,paths)
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        paths = []
        self.dfs(k,n,range(1,10),[],paths)
        return paths