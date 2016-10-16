class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        if l == r:
            return l if nums[l] >= target else l+1
        mid = (l+r)/2
        if nums[mid] - target == 0:
            return mid
        elif nums[mid] - target > 0:
            return mid if mid == l else l+self.searchInsert(nums[l:mid],target)
        else:
            return mid+1 if mid == r else mid+1+self.searchInsert(nums[mid+1:r+1],target)