class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[]] if len(nums) == 0 else self.subsets(nums[1:])+[x+[nums[0]] for x in self.subsets(nums[1:])]