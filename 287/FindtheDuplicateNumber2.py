class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s,f = nums[0],nums[nums[0]]
        while s != f:
            s,f = nums[s],nums[nums[f]]
        f = 0
        while s != f:
            s,f = nums[s],nums[f]
        return s