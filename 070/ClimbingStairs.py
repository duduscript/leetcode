class Solution(object):
    def mulMatrix(self, m1, m2):
        return [m1[0]*m2[0]+m1[1]*m2[2], m1[0]*m2[1]+m1[1]*m2[3], m1[2]*m2[0]+m1[3]*m2[2], m1[2]*m2[1]+m1[3]*m2[3] ]
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        matrix,m = [1,1,1,0],[1,0,1,0]
        while n != 0:
            if n | 1 == n:
                m = self.mulMatrix(m,matrix)
            matrix = self.mulMatrix(matrix,matrix)
            n /= 2
        return m[0]