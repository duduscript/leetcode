class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0 or k == 1:
            return nums
        else:
            rtn = [max(nums[:k])]
            for i in xrange(k,len(nums)):
                if rtn[-1]<=nums[i]:
                    rtn.append(nums[i])
                elif nums[i-k] != rtn[-1]:
                    rtn.append(rtn[-1])
                else:
                    rtn.append(max(nums[i+1-k:i+1]))
            return rtn