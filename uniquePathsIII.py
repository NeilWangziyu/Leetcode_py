class Solution:
    count = 0
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
#         find start and end
        def overall(input):
            for row in range(len(input)):
                for col in range(len(input[0])):
                    if input[row][col] == 0:
                        return False
            return True


        def DFS(i, j):
            if search_grid[i][j] == 0:
                search_grid[i][j] = 1
                if i > 0:
                    DFS(i - 1, j)
                if i < len(grid)-1:
                    DFS(i + 1, j)
                if j > 0:
                    DFS(i, j - 1)
                if j < len(grid[0])-1:
                    DFS(i, j + 1)
                search_grid[i][j] = 0
                return
            if search_grid[i][j] == 2:
                if overall(search_grid):
                    self.count += 1
                return



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    s_i, s_j = i,j
                if grid[i][j] ==2:
                    e_i, e_j = i, j

        # search_grid = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        search_grid = grid.copy()
        search_grid[s_i][s_j] = 0
        self.count = 0
        DFS(s_i, s_j)
        return self.count





input = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
s = Solution()
print(s.uniquePathsIII(input))