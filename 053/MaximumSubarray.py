class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        m = [nums[0]] * len(nums)
        for i in xrange(1,len(nums)):
            m[i] = nums[i] if m[i-1] < 0 else nums[i]+m[i-1]
        return max(m)
