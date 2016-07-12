class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums))[::-1]:
            if i == 0:
                nums.reverse()
            elif nums[i-1] < nums[i]:
                x,pos = min([[x[1],x[0]] for x in enumerate(nums[i:]) if x[1]>nums[i-1] ])
                nums[pos+i] = nums[i-1]
                nums[i-1],nums[i:] = x,sorted(nums[i:])
                break