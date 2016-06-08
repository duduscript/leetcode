l,c,size = None,None,0
def dfs_path(pos,path,target):
    for i in range(pos,size):
        if c[i] <= target :
            if target < 2*c[i]:
                if target in c:
                    l.append(path+[target])
                break
            dfs_path(i,path+[c[i]],target-c[i])
        else:
            break
class Solution(object):
    def combinationSum(self,candidates, target):
        global l,c,size
        l,c,size = [],sorted(candidates),len(candidates)
        dfs_path(0,[],target)
        return l