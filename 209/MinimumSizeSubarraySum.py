class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or sum(nums) < s:
            return 0
        left,right,sm,length = 0,0,nums[0],len(nums)
        while True:
            if sm < s:
                right = right+1
                sm = sm+nums[right]
            elif sm - nums[left] >= s:
                sm = sm-nums[left]
                left = left+1
                length = min(length,right-left+1)
            elif right != len(nums)-1:
                length = min(length,right-left+1)
                right = right+1
                sm = sm+nums[right]
            else:
                break
        return length