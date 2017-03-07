class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        else:
            left = 0
            for i in xrange(1,len(nums)):
                if nums[i] - nums[0] == i:
                    left += 1
                else:
                    break
            if left == 0:
                return [str(nums[0])]+self.summaryRanges(nums[left+1:])
            else:
                return [str(nums[0])+"->"+str(nums[left])]+self.summaryRanges(nums[left+1:])