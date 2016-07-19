class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while  l <= r:
            mid = (l+r)/2
            if nums[l] <= nums[mid] <= nums[r]:
                return nums[l]
            elif nums[mid] < nums[r]:
                r = mid
            elif l == mid:
                return nums[r]
            else:
                l = mid