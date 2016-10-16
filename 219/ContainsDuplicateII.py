class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums = sorted([[key,index] for index,key in enumerate(nums)])
        for i in xrange(len(nums) - 1):
            if nums[i][0] == nums[i+1][0] and abs(nums[i][1]-nums[i+1][1]) <= k:
                return True
        return False