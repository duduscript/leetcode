class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        for i in xrange(32):
            nums = filter(lambda x:x & 2**i==0,nums)+filter(lambda x:x & 2**i!=0,nums)
        return max(map(lambda x:nums[x]-nums[x-1],xrange(1,len(nums))))
