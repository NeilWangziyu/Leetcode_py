class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        每行的元素从左到右升序排列。
        每列的元素从上到下升序排列
        """
        def binary_search(list_t, target):
            start = 0
            end = len(list_t)-1
            mid = (start + end) // 2
            while(start<=end):
                if list_t[mid] == target:
                    return True
                else:
                    if list_t[mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                mid = (start+end) // 2
            return False


        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])

        if target < matrix[0][0] or target > matrix[row - 1][col - 1]:
            return False

        for each in matrix:
            if target>=each[0] and target<=each[-1]:
                print(each)
                if binary_search(each, target):
                    return True
        return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False

        l, r = 0, len(matrix[0]) - 1

        while l < len(matrix) and r >= 0:
            if matrix[l][r] == target:
                return True
            elif matrix[l][r] > target:
                r -= 1
            else:
                l += 1
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 5

s = Solution()
print(s.searchMatrix(matrix, target))