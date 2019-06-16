class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        # 超时 DFS
        if not grid:
            return 0
        pos = [[1,0], [0,1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1], [1, 1]]
        self.res = float('inf')
        N = len(grid)

        if N == 1:
            return 0
        if grid[0][0] == 1:
            return -1
        if grid[-1][-1] == 1:
            return -1

        check_grid = [[False for _ in range(N)]for _ in range(N)]
        check_grid[0][0] = True

        self.check_grid_count = [[float('inf') for _ in range(N)] for _ in range(N)]
        self.check_grid_count[0][0] = 1

        def DFS(x_pos, y_pos, tem_length, N, check_grid):
            # print(x_pos, y_pos)
            if tem_length >= self.res:
                return

            if tem_length <= self.check_grid_count[x_pos][y_pos]:
                self.check_grid_count[x_pos][y_pos] = tem_length
            else:
                return

            if x_pos < 0 or y_pos <0 or x_pos >=N or y_pos >= N:
                return

            if grid[x_pos][y_pos] == 1:
                return


            if x_pos == N-1 and y_pos == N-1:
                self.res = min(self.res, tem_length)
                return

            check_grid[x_pos][y_pos] = False

            for each in pos:
                if x_pos+each[0] < 0 or y_pos+each[1] < 0 or x_pos+each[0] >= N or y_pos+each[1] >= N:
                    pass
                else:
                    check_grid[x_pos+each[0]][y_pos+each[1]] = True
                    DFS(x_pos+each[0], y_pos+each[1], tem_length + 1, N, check_grid)
                    check_grid[x_pos + each[0]][y_pos + each[1]] = False


        DFS(0, 0, 1, N, check_grid)
        if self.res == float('inf'):
            return -1
        else:
            return self.res



    def shortestPathBinaryMatrix2(self, grid) -> int:
        # BFS
        if not grid:
            return 0
        pos = [[1,0], [0,1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1], [1, 1]]

        self.res = float('inf')
        N = len(grid)

        if N == 1:
            return 0
        if grid[0][0] == 1:
            return -1
        if grid[-1][-1] == 1:
            return -1

        check_grid = [[False for _ in range(N)]for _ in range(N)]
        check_grid[0][0] = True

        check_list = [[0,0,1]]
        while(check_list):
            this_check = check_list.pop(0)
            x_pos = this_check[0]
            y_pos = this_check[1]
            tem_length = this_check[2]
            if x_pos < 0 or y_pos <0 or x_pos >=N or y_pos >= N:
                continue

            if grid[x_pos][y_pos] == 1:
                continue

            if x_pos == N-1 and y_pos == N-1:
                return tem_length

            check_grid[x_pos][y_pos] = True

            for each in pos:
                if x_pos + each[0] < 0 or y_pos + each[1] < 0 or x_pos + each[0] >= N or y_pos + each[1] >= N:
                    pass
                elif check_grid[x_pos + each[0]][y_pos + each[1]] == True:
                    pass
                else:
                    check_list.append([x_pos + each[0], y_pos + each[1], tem_length + 1])

        return -1






    def shortestPathBinaryMatrix3(self, grid) :
        '''
        :param grid: : List[List[int]]
        :return: -> int
        '''
        N=len(grid)
        if grid[N-1][N-1]!=0 or grid[0][0]!=0:
            return -1
        dp = [i[:] for i in grid]
        nextsteps={(0,0)}
        nowlength = 0
        while nextsteps:
            nowlength+=1
            buffer = set()
            for nowstep in nextsteps:
                dp[nowstep[0]][nowstep[1]]=1
                if nowstep==(N-1,N-1):
                    return nowlength
                if nowstep[0]!=0:
                    if dp[nowstep[0]-1][nowstep[1]]==0:
                        buffer.add((nowstep[0]-1,nowstep[1]))
                    if nowstep[1]!=0:
                        if dp[nowstep[0] - 1][nowstep[1] - 1] == 0:
                            buffer.add((nowstep[0] - 1, nowstep[1] - 1))
                    if nowstep[1]!=N-1:
                        if dp[nowstep[0] - 1][nowstep[1] + 1] == 0:
                            buffer.add((nowstep[0] - 1,nowstep[1] + 1))
                if nowstep[1]!=0:
                    if dp[nowstep[0]][nowstep[1]-1]==0:
                        buffer.add((nowstep[0], nowstep[1]-1))
                    if nowstep[0]!=N-1:
                        if dp[nowstep[0]+1][nowstep[1]-1]==0:
                            buffer.add((nowstep[0]+1,nowstep[1]-1))
                if nowstep[0]!=N-1:
                    if dp[nowstep[0]+1][nowstep[1]]==0:
                        buffer.add((nowstep[0]+1,nowstep[1]))
                    if nowstep[1]!=N-1:
                        if dp[nowstep[0]+1][nowstep[1]+1]==0:
                            buffer.add((nowstep[0]+1,nowstep[1]+1))
                if nowstep[1]!=N-1:
                    if dp[nowstep[0]][nowstep[1]+1]==0:
                        buffer.add((nowstep[0],nowstep[1]+1))
            nextsteps=buffer
        return -1








grid = [[0,0,0],[1,1,0],[1,1,0]]
s = Solution()
print(s.shortestPathBinaryMatrix(grid))
print(s.shortestPathBinaryMatrix2(grid))
print(s.shortestPathBinaryMatrix3(grid))

grid = [[0,0,0],[0,0,0],[0,1,0]]
print(s.shortestPathBinaryMatrix(grid))
print(s.shortestPathBinaryMatrix2(grid))
print(s.shortestPathBinaryMatrix3(grid))