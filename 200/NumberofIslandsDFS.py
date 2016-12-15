class Solution(object):
    def __init__(self):
        self.flag = []
    def search(self,grid,x,y):
        if x < 0 or y < 0 or x >= len(grid) or y>=len(grid[x]) or self.flag[x][y] or grid[x][y] == '0':
            return
        self.flag[x][y] = 1
        self.search(grid,x-1,y)
        self.search(grid,x+1,y)
        self.search(grid,x,y-1)
        self.search(grid,x,y+1)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        for i in range(len(grid)):
            self.flag.append([0]*len(grid[i]))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if self.flag[i][j] == 0 and grid[i][j] == '1':
                    islands += 1
                    self.search(grid,i,j)
        return islands