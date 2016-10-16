class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        size = len(nums)
        for i in xrange(0,size):
            if target - nums[i] in t:
                return t[target - nums[i]],i
            t[nums[i]] = i