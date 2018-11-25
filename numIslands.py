class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def DFS(row, col, count):
            if grid[row][col] == "1":
                if new_grid[row][col] == 0:
                    new_grid[row][col] = count
                    if row < total_row - 1:
                        DFS(row + 1, col, count)
                    if col < total_col - 1:
                        DFS(row, col + 1, count)
                    if row > 0:
                        DFS(row - 1, col, count)
                    if col > 0:
                        DFS(row, col - 1, count)
                else:
                    # 已经被统计过
                    return
            else:
                #         grid 的海域
                new_grid[row][col] = "0"
                return





        if not grid:
            return 0
        if grid == [[0]]:
            return 0
        if grid == [[1]]:
            return 1
        new_grid = []
        total_row = len(grid)
        total_col = len(grid[0])
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append(0)
            new_grid.append(row)


        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if new_grid[i][j] == 0:
                    if grid[i][j] == "1":
                        print(i, j)
                        count += 1
                        DFS(i, j, count)
                        print(new_grid)



        print(new_grid)
        return count


s = Solution()
print(s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))