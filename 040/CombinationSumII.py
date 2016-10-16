class Solution(object):
    def dfs(self,paths,candidates,target,path,index):
        if target == 0:
            paths.append(path)
        elif target < 0:
            return
        else:
            for i in xrange(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                self.dfs(paths,candidates,target-candidates[i],path+[candidates[i]],i+1)
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        paths = []
        self.dfs(paths,sorted(filter(lambda x:x<=target,candidates)),target,[],0)
        return paths