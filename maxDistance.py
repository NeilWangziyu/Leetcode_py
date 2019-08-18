from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        land_stack = []
        row =len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    land_stack.append([i, j])


        if not land_stack:
            return -1
        if len(land_stack) == row*col:
            return -1
        c = -1
        while(True):
            c += 1
            next_sea = []
            for each_land in land_stack:
                x = each_land[0]
                y = each_land[1]
                if x > 0:
                    if grid[x-1][y] == 0:
                        grid[x-1][y] = 1
                        next_sea.append([x-1,y])
                if y > 0:
                    if grid[x][y-1] == 0:
                        grid[x][y-1] = 1
                        next_sea.append([x,y-1])
                if x < row - 1:
                    if grid[x+1][y] == 0:
                        grid[x+1][y] = 1
                        next_sea.append([x+1,y])
                if y < col - 1:
                    if grid[x][y+1] == 0:
                        grid[x][y+1] = 1
                        next_sea.append([x,y+1])
            print(next_sea)
            if not next_sea:
                return c
            else:
                land_stack = next_sea






s = Solution()
grid = [[1,0,1],[0,0,0],[1,0,1]]
print(s.maxDistance(grid))

grid = [[1,0,0],[0,0,0],[0,0,0]]
print(s.maxDistance(grid))

grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(s.maxDistance(grid))

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(s.maxDistance(grid))