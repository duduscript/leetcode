class Solution(object):
    def __init__(self):
        self.rtn = []
    def getline(self, matrix, flag):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        if flag == 1:
            self.rtn += matrix[0]
            self.getline(matrix[1:],2)
        elif flag == 2:
            self.rtn += map(lambda vec:vec[-1],matrix)
            self.getline(map(lambda vec:vec[:-1],matrix),3)
        elif flag == 3:
            self.rtn += matrix[-1][::-1]
            self.getline(matrix[:-1],4)
        else:
            self.rtn += map(lambda vec:vec[0],matrix)[::-1]
            self.getline(map(lambda vec:vec[1:],matrix),1)
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.getline(matrix,1)
        return self.rtn