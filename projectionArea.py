class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total_base = 0
        total_left = [0 for _ in range(len(grid))]
        total_right = [0 for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    total_base += 1
                if grid[i][j] > total_left[i]:
                    total_left[i] = grid[i][j]
                if grid[i][j] > total_right[j]:
                    total_right[j] = grid[i][j]
        return total_base + sum(total_left) + sum(total_right)


