class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix

        row = []
        for i in range(len(matrix)):
            row.append(1)
        col = []
        for j in range(len(matrix[0])):
            col.append(1)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        print(row, col)

        for index, value in enumerate(row):
            if value == 0:
                # print(index)
                for each in range(len(matrix[index])):
                    print(each)
                    matrix[index][each] = 0

        for index, value in enumerate(col):
            if value == 0:
                for each in range(len(matrix)):
                    matrix[each][index] = 0
        print(matrix)

        # another solution,
        iTemp = set()
        jTemp = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    iTemp.add(i)
                    jTemp.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in iTemp or j in jTemp:
                    matrix[i][j] = 0



m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s = Solution()
print(s.setZeroes(m))