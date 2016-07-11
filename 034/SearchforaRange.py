class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r,mid = 0,len(nums),0
        while l < r:
            mid = (l+r)/2
            if nums[mid]- target == 0:
                break
            elif nums[mid] - target <0:
                l = mid+1
            else:
                r = mid
        if l >= r:
            return [-1,-1]
        r=l=mid
        while l > 0 and nums[l-1] == target:
            l -= 1
        while r < len(nums)-1 and nums[r+1] == target:
            r += 1
        return [l,r]
            