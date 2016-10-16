class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        vec = [1]
        for _ in xrange(rowIndex):
            vec =[1] + [vec[i]+vec[i-1] for i in xrange(1,len(vec))] +[1]
        return vec