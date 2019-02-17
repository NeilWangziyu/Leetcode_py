class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        if not grid:
            return -1

        row = len(grid)
        col = len(grid[0])
        rotten = []
        fresh = set()
        MAX_length = 10000
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten.append([i, j])
                elif grid[i][j] == 1:
                    fresh.add(i*MAX_length+j)
        print(rotten)
        print(fresh)
        count = 0
        while(rotten):
            new_rotten = []
            for i in range(len(rotten)):
                each = rotten[i]
                if each[0] > 0:
                    if (each[0]-1)*MAX_length+each[1] in fresh:
                        print((each[0]-1)*MAX_length+each[1])
                        fresh.remove((each[0]-1)*MAX_length+each[1])
                        new_rotten.append([each[0]-1, each[1]])
                if each[0] < row - 1:
                    if (each[0]+1)*MAX_length+each[1] in fresh:
                        fresh.remove((each[0]+1)*MAX_length+each[1])
                        new_rotten.append([each[0]+1, each[1]])

                if each[1] > 0:
                    if (each[0])*MAX_length+each[1]-1 in fresh:
                        fresh.remove((each[0])*MAX_length+each[1]-1)
                        new_rotten.append([each[0], each[1]-1])
                if each[1] < col - 1:
                    if (each[0])*MAX_length+each[1]+1 in fresh:
                        fresh.remove((each[0])*MAX_length+each[1]+1)
                        new_rotten.append([each[0], each[1]+1])
            if new_rotten != []:
                count += 1
            rotten = new_rotten

        if len(fresh)!=0:
            return -1
        else:
            return count




grid = [[0,2]]

s = Solution()
print(s.orangesRotting(grid))