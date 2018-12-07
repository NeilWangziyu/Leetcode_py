class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [[]]:
            return []

        row = len(matrix)
        col = len(matrix)
        res = []
        if row == col:
            for i in range(row):
                for row in range(i+1):
                    res.append(matrix[row][i-row])
                    print(matrix[row][i-row])



s = Solution()
print(s.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))




