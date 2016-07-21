class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in xrange(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]