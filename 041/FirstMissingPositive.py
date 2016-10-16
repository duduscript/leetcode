class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(filter(lambda x:x>0,nums)))
        for i in xrange(len(nums)):
            while nums[i] <= len(nums) and nums[i] != i+1:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
        for i in xrange(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1