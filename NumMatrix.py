class NumMatrix:
    dp = None
    def __init__(self, matrix):
        # dp[i][j]表示前i行前j列的矩形的和
        # sum(sx, sy, ex, ey) = dp[ex][ey] - dp[sx][sy] - (dp[ex][sy] - dp[sx][sy] + dp[sx][ey] - dp[sx][sy])
        if len(matrix) == 0:
            pass
        else:
            row_length = len(matrix)
            col_length = len(matrix[0])
            self.dp = [[0 for _ in range(col_length+1)] for _ in range(row_length+1)]
            for i in range(1, len(matrix)+1):
                # row
                for j in range(1, len(matrix[0])+1):
                 # col
                    self.dp[i][j] = matrix[i - 1][j - 1] + self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp:
            return 0
        return self.dp[row2+1][col2+1] - self.dp[row1][col1] - (self.dp[row1][col2+1] + self.dp[row2+1][col1] - 2 * self.dp[row1][col1])


class NumMatrix01:

    def __init__(self, matrix):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i][j] = self.matrix[i][j] + (self.matrix[i - 1][j] if i > 0 else 0) + (
                    self.matrix[i][j - 1] if j > 0 else 0) - (self.matrix[i - 1][j - 1] if i > 0 and j > 0 else 0)

    def sumRegion(self, row1, col1, row2, col2):
        return self.matrix[row2][col2] + (self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0) - (
            self.matrix[row2][col1 - 1] if col1 > 0 else 0) - (self.matrix[row1 - 1][col2] if row1 > 0 else 0)


class NumMatrix0:
    mat = None
    def __init__(self, matrix):
        self.mat = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # if row1 == row2 and col1 == col2 and row1 == col1:
        #     return self.mat[row1][col1]
        if row1 != row2:
            return self.sumRegion(row1, col1, row1, col2) + self.sumRegion(row1+1, col1, row2, col2)
        elif col1 != col2:
            return self.sumRegion(row1,col1, row2,col1) + self.sumRegion(row1, col1+1, row2,col2)
        else:
            return self.mat[row1][col2]


class NumMatrix2:
    mat = None
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.mat = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2 + 1):
            # for j in range(col1, col2+1):
            res += sum(self.mat[i][col1:col2 + 1])
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [[3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]]


s = NumMatrix(matrix)
s2 = NumMatrix2(matrix)

print(s.sumRegion(0, 0, 0, 0))
print(s2.sumRegion(0, 0, 0, 0))

print(s.sumRegion(2, 1, 4, 3))
print(s2.sumRegion(2, 1, 4, 3))

print(s.sumRegion(1, 1, 2, 2))
print(s2.sumRegion(1, 1, 2, 2))

print(s.sumRegion(1, 2, 2, 4))

print(s2.sumRegion(1, 2, 2, 4))
