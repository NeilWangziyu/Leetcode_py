class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        ordered
        """

        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])

        if target < matrix[0][0] or target > matrix[row - 1][col - 1]:
            return False

        start = 0
        end = row
        mid_row = row // 2
        # print(not (target>=matrix[mid_row][0] and target<=matrix[mid_row][col-1]))


        while((target<matrix[mid_row][0] or target>matrix[mid_row][col-1]) and start<=end):
            # print(matrix[mid_row][0],matrix[mid_row][col-1])
            if target < matrix[mid_row][0]:
                end = mid_row - 1
                mid_row = (start + end) // 2
                # print(mid_row)
            else:
                # target < matrix[mid_row][col-1]
                start = mid_row + 1
                mid_row = (start + end) // 2
                # print(mid_row)

        if start>end:
            return False
        else:
            # print(start, end, mid_row)
            pass
        start = 0
        end = col
        mid_col = (start + end)//2
        while(start<=end and matrix[mid_row][mid_col]!=target):
            # print(start, end, mid_col)
            if matrix[mid_row][mid_col]< target:
                start = mid_col+1
                mid_col = (start+end) // 2
            else:
                end = mid_col -1
                mid_col = (start + end) // 2

        if matrix[mid_row][mid_col]==target:
            return True
        else:
            return False








target = 5

#
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]




s = Solution()
print(s.searchMatrix(matrix, target))
# print(s.searchMatrix(matrix2, target2))




