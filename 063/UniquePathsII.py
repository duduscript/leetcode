class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid = [[0] * len(obstacleGrid[0])] * len(obstacleGrid)
        for i in xrange(len(obstacleGrid)):
            grid[i][0] = 1 if obstacleGrid[i][0] == 0 and (i == 0 or grid[i-1][0] != 0) else 0
            for j in xrange(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                elif i == 0:
                    grid[i][j] = grid[i][j-1]
                else:
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]
        return grid[-1][-1]