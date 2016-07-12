class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x,y = reduce(lambda x,y:x^y,nums),1
        while x&y != y:
            y <<= 1
        c1,c2 = 0,0
        for z in nums:
            if z&y == y:
                c1 ^= z
            else:
                c2 ^= z
        return [c1,c2]