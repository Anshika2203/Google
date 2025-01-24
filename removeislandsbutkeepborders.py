class Graph:
    def __init__(self, row, col, grid):
        self.row=row
        self.col=col
        self.grid=grid


    def checkBorder(self,r,c,grid):
        if not grid[r][c-1] or not grid[r][c+1] or not grid[r-1][c] or not grid[r+1][c] or not grid[r-1][c-1] or not grid[r+1][c+1] or not grid[r-1][c+1] or not grid[r+1][c-1]:
            return False
        else:
            return True

# executes in 2 passes, set element to -1 then replace with 0
    def deleteIsland(self):
        for r in range(1,row):
            for c in range(1,col):
                #print(self.grid[r][c], r, c)
                if self.grid[r][c]==1 and self.checkBorder(r,c,self.grid):
                    #print(r,c)
                    self.grid[r][c]=-1
        for r in range(1, row):
            for c in range(1, col):
                if self.grid[r][c]==-1:
                    self.grid[r][c]=0
        return self.grid

# make a copy of the list, executes in 1 pass
    def deleteIsland2(self):
        temp=list(self.grid)
        for r in range(1,row):
            for c in range(1,col):
                #print(self.grid[r][c], r, c)
                if temp[r][c]==1 and self.checkBorder(r,c,temp):
                    #print(r,c)
                    self.grid[r][c]=0
        # for r in range(1, row):
        #     for c in range(1, col):
        #         if self.grid[r][c]==-1:
        #             self.grid[r][c]=0
        return self.grid





grid = [[0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]]

row=len(grid)-1
col=len(grid[0])-1

grid = Graph(row,col,grid)

print("One: {}".format(grid.deleteIsland()))
print("Two: {}".format(grid.deleteIsland2()))


grid2=[[1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1]]


row=len(grid2)-1
col=len(grid2[0])-1

grid2 = Graph(row,col,grid2)

print("One: {}".format(grid2.deleteIsland()))
print("Two: {}".format(grid2.deleteIsland2()))


grid3 = [[1, 1, 1, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 1, 1],
 [0, 0, 0, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 1, 1]]

row=len(grid3)-1
col=len(grid3[0])-1

grid3 = Graph(row,col,grid3)

print("One: {}".format(grid3.deleteIsland()))
print("Two: {}".format(grid3.deleteIsland2()))