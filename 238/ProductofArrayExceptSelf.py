class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_num = len(filter(lambda x:x==0,nums))
        if zero_num == 0:
            pro = reduce(lambda x,y:x*y,nums)
            return map(lambda x:pro/x,nums)
        elif zero_num == 1:
            pro = reduce(lambda x,y:x*y,filter(lambda x:x!=0,nums))
            return map(lambda x:0 if x!=0 else pro,nums)
        else:
            return [0]*len(nums)