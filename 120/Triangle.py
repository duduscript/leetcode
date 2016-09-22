class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for line in xrange(len(triangle)):
            if line == 0:
                continue
            for pos in xrange(line+1):
                if pos == 0 or pos == line:
                    triangle[line][pos] += triangle[line-1][0 if pos == 0 else line-1]
                else:
                    triangle[line][pos] += min(triangle[line-1][pos],triangle[line-1][pos-1])
        return min(triangle[-1])