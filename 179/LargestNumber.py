class Solution:
    # @param {integer[]} nums
    # @return {string}
    def cmp(self, x1, x2):
        l1,l2 = len(x1),len(x2)
        x1,x2 = x1*l2,x2*l1
        if x1 > x2:
            return -1
        elif x1 < x2:
            return 0
        else:
            return 1
    def largestNumber(self, nums):
        return str(int(''.join(sorted(map(str,nums),cmp=self.cmp))))