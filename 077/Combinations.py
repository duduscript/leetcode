class Solution(object):
    def dfs(self, paths, path, s,k):
        if k == 0:
            paths.append(path)
        else:
           for i in xrange(len(s)):
               self.dfs(paths,path+[s[i]],s[i+1:],k-1)
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        paths = []
        if k <= n/2:
            self.dfs(paths,[],range(1,n+1),k)
        else:
            self.dfs(paths,[],range(1,n+1),n-k)
            for i in xrange(len(paths)):
                paths[i] = list(set(range(1,n+1)) - set(paths[i]))
        return paths