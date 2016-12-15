import Queue
class Solution(object):
    def __init__(self):
        self.flag = []
    def search(self,grid,x,y):
        q = Queue.Queue()
        q.put((x,y))
        while not q.empty():
            x,y = q.get()
            if x < 0 or y < 0 or x >= len(grid) or y>=len(grid[x]) or self.flag[x][y] or grid[x][y] == '0':
                continue
            self.flag[x][y] = 1
            q.put((x-1,y))
            q.put((x+1,y))
            q.put((x,y-1))
            q.put((x,y+1))
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