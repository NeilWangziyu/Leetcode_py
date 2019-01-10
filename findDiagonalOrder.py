class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_len = len(matrix)
        if row_len == 0:
            return []
        col_len = len(matrix[0])
        result = [0 for _ in range(row_len * col_len)]

        flag = True
        i = 0
        j = 0
        index = 0
        while i != row_len - 1 or j != col_len - 1:
            result[index] = matrix[i][j]
            index += 1

            if flag:
                if i - 1 >= 0 and j + 1 < col_len:
                    i -= 1
                    j += 1

                else:
                    if j + 1 < col_len:
                        j += 1
                        flag = not flag
                    else:
                        i += 1
                        flag = not flag

            else:
                if i + 1 < row_len and j - 1 >= 0:
                    i += 1
                    j -= 1
                else:
                    if i + 1 < row_len:
                        i += 1
                        flag = not flag
                    else:
                        j += 1
                        flag = not flag

        result[index] = matrix[i][j]
        return result


s = Solution()
print(s.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [10, 11, 12]
]))




