class Solution:
    grid = []
    def numEnclaves(self, A) -> int:
        def DFS(x, y, row, col):
            # x:row, y:col
            if A[x][y]== 1 and not self.grid[x][y]:
                self.grid[x][y] = True
                if x > 0:
                    DFS(x-1, y, row, col)
                if y > 0:
                    DFS(x, y-1, row, col)
                if x < row - 1:
                    DFS(x+1, y, row, col)
                if y < col - 1:
                    DFS(x, y + 1, row, col)

        if not A:
            return 0

        row = len(A)
        col = len(A[0])
        self.grid = [[False for _ in range(col)] for _ in range(row)]

        for i in range(col):
            if A[0][i] == 1:
                DFS(0, i, row, col)
            if A[row-1][i] == 1:
                DFS(row-1, i, row, col)

        for j in range(1, row-1):
            if A[j][0] == 1:
                DFS(j, 0, row, col)
            if A[j][col-1] == 1:
                DFS(j, col-1, row, col)
        res = 0
        for j in range(1, row-1):
            for i in range(1, col-1):
                if A[j][i] == 1 and self.grid[j][i] == False:
                    res += 1
        return res




A = [[0,0,1,1,0,0,0,0,0,1],[1,1,0,1,0,0,1,0,0,1],[1,1,0,0,1,0,1,1,0,0],[1,0,0,1,0,0,0,0,0,1],[0,0,1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,1,0,1,1,1,0,1,0],[0,1,1,1,0,0,1,0,0,1],[0,1,1,0,0,1,0,1,1,0],[1,0,1,1,0,0,1,1,0,0],[1,0,1,0,1,1,1,0,0,1]]
s = Solution()
print(s.numEnclaves(A))


