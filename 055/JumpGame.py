class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        border = 1
        for i in xrange(len(nums)):
            if i+1 > border:
                break
            if i + 1 + nums[i] > border:
                border = i + 1 + nums[i]
        return border >= len(nums)