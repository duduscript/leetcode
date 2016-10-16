class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tail1,tail2,tail = m-1,n-1,m+n-1
        while tail1 >= 0 and tail2 >= 0:
            if nums1[tail1] >= nums2[tail2]:
                nums1[tail] = nums1[tail1]
                tail,tail1 = tail-1,tail1-1
            else:
                nums1[tail] = nums2[tail2]
                tail,tail2 = tail-1,tail2-1
        if tail1 < 0:
            for i in xrange(tail2+1):
                nums1[i] = nums2[i]