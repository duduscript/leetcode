class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        vec = [vec[0] for vec in matrix]
        vec.append(float('inf'))
        l,mid,r = 0,0,len(vec)-1
        while l < r:
            mid = (l+r)/2
            if vec[mid] > target:
                r = mid
            elif vec[mid+1] <= target:
                l = mid + 1
            else:
                break
        l,r = 0,len(matrix[mid])
        while l < r:
            m = (l+r)/2
            if matrix[mid][m] > target:
                r = m
            elif matrix[mid][m] <target:
                l = m + 1
            else:
                return True
        return False