class Solution(object):
    def swap(self, matrix, c, r, val):
        tmp = matrix[c][r]
        matrix[c][r] = val
        return tmp
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        col,row = (n/2,n/2) if n%2 == 0 else (n/2,n/2+1)
        for i in xrange(col):
            for j in xrange(row):
                tmp = matrix[n-1-j][i]
                for k in xrange(4):
                    if k == 0:
                        tmp = self.swap(matrix,i,j,tmp)
                    elif k == 1:
                        tmp = self.swap(matrix,j,n-1-i,tmp)
                    elif k == 2:
                        tmp = self.swap(matrix,n-1-i,n-1-j,tmp)
                    else:
                        tmp = self.swap(matrix,n-1-j,i,tmp)