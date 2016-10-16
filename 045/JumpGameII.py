class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r,time,m = 0,1,0,0
        while m < len(nums)-1:
            tmp = map(lambda x:min(len(nums)-1,nums[x]+x),xrange(l,r))
            if tmp == []:
                return 0
            m = max(tmp)
            l,r,time = r,m+1,time+1
        return time