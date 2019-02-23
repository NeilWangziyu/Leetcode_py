class Solution:
    def numMagicSquaresInside(self, grid: 'List[List[int]]') -> 'int':
        def check(i, j, grid):
            set_m = set([grid[i][j], grid[i+1][j] ,grid[i+2][j], grid[i][j+1] , grid[i+1][j+1],grid[i+2][j+1],grid[i][j+2] , grid[i+1][j+2],grid[i+2][j+2]])
            if set_m != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
            col_v_1 = (grid[i][j] + grid[i+1][j] + grid[i+2][j])
            col_v_2 = (grid[i][j+1] + grid[i+1][j+1]+grid[i+2][j+1])
            col_v_3 = (grid[i][j+2] + grid[i+1][j+2]+grid[i+2][j+2])
            row_v_1 = (grid[i][j] +grid[i][j+1] +grid[i][j+2])
            row_v_2 = (grid[i+1][j] +grid[i+1][j+1] +grid[i+1][j+2])
            row_v_3 = (grid[i+2][j] +grid[i+2][j+1] +grid[i+2][j+2])
            left = (grid[i][j] + grid[i+1][j+1] +grid[i+2][j+2])
            right = (grid[i+2][j] +grid[i+1][j+1] +grid[i][j+2])
            if col_v_1 == col_v_2 == col_v_3 == row_v_1 == row_v_2 == row_v_3 == left == right:
                return True
            else:
                return False

        res = 0

        if len(grid) < 3 or len(grid[0]) < 3:
            return res
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                print(i, j)
                if check(i, j, grid):

                    res += 1
        return res


grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]

s = Solution()
print(s.numMagicSquaresInside(grid))