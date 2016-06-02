class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        d1,d2,size = {},{},len(nums)
        for i in xrange(0,size-2):
            if nums[i] in d2:
                continue
            d2[nums[i]] = 1
            if nums[i] > 0:
                break
            for j in xrange(i+1,size-1):
                if nums[i]+nums[j] > 0:
                    break
                if -(nums[i]+nums[j]) in nums[j+1:]:
                    d1[(nums[i],nums[j],-(nums[i]+nums[j]))] = 1
        return d1.keys()