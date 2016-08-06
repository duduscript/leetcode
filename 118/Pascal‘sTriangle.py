class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        matrix,vec = [],[1]
        for _ in xrange(numRows):
            matrix.append(vec)
            vec = [1] + [vec[i]+vec[i-1] for i in xrange(1,len(vec))] + [1]
        return matrix