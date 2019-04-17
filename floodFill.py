class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return
        row =  len(image)
        col =  len(image[0])
        check_grid = [[False for _ in range(col)] for _ in range(row)]

        def DFS(i, j, old_c, c):
            if check_grid[i][j] == True:
                return
            else:
                check_grid[i][j] = True
                image[i][j] = c
                if i > 0:
                    if image[i-1][j] == old_c:
                        DFS(i-1, j, old_c, c)
                if i < row-1:
                    if image[i + 1][j] == old_c:
                        DFS(i + 1, j, old_c, c)

                if j > 0:
                    if image[i][j - 1] == old_c:
                        DFS(i, j - 1, old_c, c)
                if j < col - 1:
                    if image[i][j + 1] == old_c:
                        DFS(i, j + 1, old_c, c)
                return
        DFS(sr, sc, image[sr][sc], newColor)
        return image




if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    s = Solution()
    print(s.floodFill(image, sr, sc, newColor))

    image =[[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 1
    print(s.floodFill(image, sr, sc, newColor))


