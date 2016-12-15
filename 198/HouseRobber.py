class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:return 0
        foo = [0]*len(nums)
        for i in range(len(nums)):
            if i+2 < len(nums) and nums[i]+foo[i]>foo[i+2]:
                foo[i+2] = nums[i]+foo[i]
            if i+3 < len(nums) and nums[i]+foo[i]>foo[i+3]:
                foo[i+3] = nums[i]+foo[i]
        return max(map(lambda i:nums[i]+foo[i],range(len(nums))))