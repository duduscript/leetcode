class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for index in xrange(len(nums)):
            if nums[index] != 0:
                nums[pos] = nums[index]
                if index != pos:nums[index] = 0
                pos += 1
