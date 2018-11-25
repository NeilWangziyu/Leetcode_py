class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def DFS(row, col):
            island_area = 0
            if grid[row][col] == 1:
                if new_grid[row][col] == 0:
                    new_grid[row][col] = 1
                    island_area += 1
                    if row < total_row - 1:
                        island_area += DFS(row + 1, col)
                    if col < total_col - 1:
                        island_area += DFS(row, col + 1)
                    if row > 0:
                        island_area += DFS(row - 1, col)
                    if col > 0:
                        island_area += DFS(row, col - 1)
                    return island_area
                else:
                    # 已经被统计过
                    return 0
            else:
                #         grid 的海域
                new_grid[row][col] = "0"
                return 0

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

        max_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if new_grid[i][j] == 0:
                    if grid[i][j] == 1:
                        print(i, j)
                        this_island_area = DFS(i, j)
                        # print(new_grid)
                        if this_island_area > max_island:
                            max_island = this_island_area
        return max_island


s = Solution()
print(s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))