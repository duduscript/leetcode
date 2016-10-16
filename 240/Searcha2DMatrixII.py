class Solution(object):
    def searchInMatrix(self, matrix, target,col_left,row_left,col_right,row_right):
        if col_left >= col_right or row_left >= row_right:
            return False
        col_mid,row_mid = (col_right-col_left)/2+col_left,0
        l,r = row_left,row_right
        while l < r:
            row_mid = (r-l)/2+l
            if matrix[col_mid][row_mid] > target:
                r = row_mid
            elif matrix[col_mid][row_mid+1] <= target:
                l = row_mid+1
            elif matrix[col_mid][row_mid] == target:
                return True
            else:
                return self.searchInMatrix(matrix,target,col_mid+1,row_left,col_right,row_mid+1) or self.searchInMatrix(matrix,target,col_left,row_mid+1,col_mid,row_right)
        return self.searchInMatrix(matrix,target,col_left,row_left,col_mid,row_right)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        matrix = map(lambda x:x+[float('inf')],matrix)
        return self.searchInMatrix(matrix,target,0,0,len(matrix),len(matrix[0])-1)