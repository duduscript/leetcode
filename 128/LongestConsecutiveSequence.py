class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic,dic1,dic2 = {},{},{}
        for x in nums:
            dic[x],dic1[x],dic2[x] = 1,x,x
        for x in dic.keys():
            if x-1 in dic:
                dic1[x] = dic1[x-1]
                dic2[dic1[x]] = x
            if x+1 in dic:
                dic1[dic2[x+1]] = dic1[x]
                dic2[dic1[x]] = dic2[x+1]
        return max([x-dic1[x] for x in dic1.keys()])+1