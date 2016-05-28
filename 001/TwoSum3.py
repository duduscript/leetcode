class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = sorted([ [x,i] for i,x in enumerate(nums)])
        print(l)
        size = len(nums)
        dic = {}
        for i in range(0,size):
            if not target - l[i][0] in dic:
                dic[l[i][0]] = l[i]
            else:
                return dic[target - l[i][0]][1],l[i][1]