class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col,row = set(),set()
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    col.add(i)
                    row.add(j)
        for i in xrange(len(matrix)):
            if i in col:
                for j in xrange(len(matrix[0])):
                    matrix[i][j] = 0
        for j in xrange(len(matrix[0])):
            if j in row:
                for i in xrange(len(matrix)):
                    matrix[i][j] = 0