def combinationSum(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res

def dfs(nums, target, index, path, res):
    print(path,target)
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in xrange(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)

print(combinationSum([20,23,25,37,33,41,27,45,30,35,44,32,46,28,29,43,34,26,42,24,39,22,38,31,48,21,36,47,49],68))
