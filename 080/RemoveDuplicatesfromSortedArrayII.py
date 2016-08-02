class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = [pair[1] for pair in enumerate(nums) if pair[0]<2 or pair[1] != nums[pair[0]-1] or pair[1] != nums[pair[0]-2]]
        for i in xrange(len(p)):
            nums[i] = p[i]
        return len(p)