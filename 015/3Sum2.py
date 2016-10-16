class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        d1,d2,size = {},{},len(nums)
        for i in xrange(0,size-2):
            d3 = {}
            if nums[i] in d2:
                continue
            d2[nums[i]] = 1
            if nums[i] > 0:
                break
            for j in xrange(i+1,size-1):
                if nums[j] in d3:
                    continue
                d3[nums[j]] = 1
                tmp = nums[i] + nums[j]
                if tmp > 0:
                    break
                if -tmp in nums[j+1:]:
                    d1[(nums[i],nums[j],-tmp)] = 1
        return d1.keys()