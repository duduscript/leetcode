class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,dic = len(nums)/2+len(nums)%2,{}
        for i in nums:
            dic[i] = dic[i]+1 if i in dic else 1
            if dic[i] >= l:
                return i