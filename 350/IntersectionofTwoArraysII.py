class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1,nums2,r = sorted(nums1),sorted(nums2),[]
        l1,l2,s1,s2 = 0,0,len(nums1),len(nums2)
        while l1<s1 and l2<s2:
            if nums1[l1] == nums2[l2]:
                r.append(nums1[l1])
                l1,l2 = l1+1,l2+1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return r