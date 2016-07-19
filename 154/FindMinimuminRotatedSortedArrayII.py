class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)/2
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return nums[l]