class Solution(object):
    def numIslands(self, grid):
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == '1'):
                    numIslands += self.removeIslands(grid,i,j)
        return numIslands
    def removeIslands(self, grid, i , j):
        try:
            if (i<0 or i>len(grid) or j<0 or j>len(grid[i]) or grid[i][j]=='0'):
                return 0
        except:
            return 0
        grid[i][j] = '0'
        self.removeIslands(grid,i+1,j)
        self.removeIslands(grid,i-1,j)
        self.removeIslands(grid,i,j+1)
        self.removeIslands(grid,i,j-1)
        return 1
