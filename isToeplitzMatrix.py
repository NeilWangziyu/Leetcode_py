class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return False
        if len(matrix)==1:
            return True
        if len(matrix[0])==1:
            return True

        row = len(matrix)
        col = len(matrix[0])

        if col >= row:
            for i in range(col):
                test = matrix[0][i]
                j = 0
                if i < (col - row + 1):
                    while(j < row):
                        if matrix[j][j+i] != test:
                            return False
                        j += 1
                else:
                    while(j < col - i):
                        if matrix[j][i+j] != test:
                            return False
                        j += 1


            for i in range(1, row):
                test = matrix[i][0]
                j = 0
                while(j<row-i):
                    if matrix[i+j][j] != test:
                        return False
                    j += 1
            return True

        else:
            for i in range(row):
                print(i)
                test = matrix[i][0]
                j = 0
                if i<(row-col+1):
                    print(matrix[i+j][j])
                    while(j<col):
                        if matrix[i+j][j] != test:
                            return False
                        j += 1
                else:
                    while(j < row - i):
                        if matrix[i+j][j] != test:
                            return False
                        j += 1

            for i in range(1, col):
                print("i2",i)
                test = matrix[0][i]
                j = 0
                while(j<col-i):
                    if matrix[j][i+j] != test:
                        return False
                    j += 1
            return True

    def isToeplitzMatrix2(self, matrix):
#         检查每个值是否等于其左上角的值
        if not matrix:
            return False
        if len(matrix)==1:
            return True
        if len(matrix[0])==1:
            return True
        row = len(matrix)
        col = len(matrix[0])

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True




# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]

matrix = [[97,97],[80,97],[10,80]]
s = Solution()
print(s.isToeplitzMatrix2(matrix))