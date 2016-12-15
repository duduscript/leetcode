class Solution(object):
    def __init__(self):
        self.flag = []
    def rotate_num(self,i,nums,k):
        pos = nums[i]
        while self.flag[(i+k)%len(nums)] == 0:
            self.flag[(i+k)%len(nums)] = 1
            pos,nums[(i+k)%len(nums)] = nums[(i+k)%len(nums)],pos
            i = (i+k)%len(nums)
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.flag = [0]*len(nums)
        for i in range(len(nums)):
            self.rotate_num(i,nums,k)