class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = []
        nums.sort()
        if target > 0 and sum(nums[-4:]) <target:
            return l
        if target <0 and sum(nums[0:4]) >target:
            return l
        for i in xrange(0,len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if target > 0 and nums[i]>target:
                break
            for j in xrange(i+1,len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                if target > 0 and nums[i]+nums[j]>target:
                    break
                for k in xrange(j+1,len(nums)-1):
                    if k != j+1 and nums[k] == nums[k-1]:
                        continue
                    tmp = nums[i]+nums[j]+nums[k]
                    if target > 0 and tmp > target:
                        break
                    if target-tmp in nums[k+1:]:
                        l.append([nums[i],nums[j],nums[k],target-tmp])
        return l