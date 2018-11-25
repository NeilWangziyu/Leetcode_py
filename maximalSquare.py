class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        print(row, col)

        # new_mat = [["0" for _ in range(col)] for _ in range(row)]

        def search_for_max(i, j, level):
            if (i+level)<row and (j+level)<col:
                for each in matrix[i+level][j:j+level+1]:
                    print("each", each)
                    if each != 1:
                        return False

                for each in matrix[i:i+level]:
                    print("each2", each)
                    if each[j+level] != 1:
                        return False

                return True

            else:
                return False


        max_square = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    pass
                else:
                    print(matrix[r][c], r, c)
                    level = 1
                    while(search_for_max(r, c, level)):
                        level += 1
                    if level > max_square:
                        max_square = level

        return max_square**2



matrix = [[1,0, 1, 0, 0],[1, 0, 1, 1, 1], [1, 1, 1, 1, 1,],[1, 0, 0, 1, 0]]
s = Solution()
print(s.maximalSquare(matrix))