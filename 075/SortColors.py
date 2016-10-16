class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colors = [0]*3
        for i in xrange(len(nums)):
            colors[nums[i]] += 1
        for i in xrange(3):
            l = 0 if i==0 else sum(colors[0:i])
            for j in xrange(l,l+colors[i]):
                nums[j] = i
