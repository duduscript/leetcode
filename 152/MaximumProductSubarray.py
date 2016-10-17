class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if nums[0] == 0:
            return max(0,self.maxProduct(nums[1:]))
        noneg = True if nums[0]>0 else False
        oneneg = not noneg
        positive = [nums[0]]*len(nums) if nums[0]>0 else [1]*len(nums)
        negative = [-1]*len(nums) if nums[0]>0 else [nums[0]]*len(nums)
        for i in xrange(1,len(nums)):
            if nums[i] > 0:
                positive[i] = positive[i-1]*nums[i]
                if not noneg:
                    negative[i] = negative[i-1]*nums[i]
            elif nums[i]<0:
                if noneg:
                    negative[i],positive[i] = positive[i-1]*nums[i],1
                else:
                    positive[i],negative[i] = negative[i-1]*nums[i],positive[i-1]*nums[i]
                noneg = False
            else:
                return max(nums[0],self.maxProduct(nums[i:])) if oneneg else max(max(positive[:i]),self.maxProduct(nums[i:]))
            oneneg = False
        return max(positive)
