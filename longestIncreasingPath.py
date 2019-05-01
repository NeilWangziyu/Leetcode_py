from functools import reduce
# 对sequence连续使用function, 如果不给出initial, 则第一次调用传递sequence的两个元素,
# 以后把前一次调用的结果和sequence的下一个元素传递给function. 如果给出initial,
# 则第一次传递initial和sequence的第一个元素给function.
class Solution:
    longest = 0
    def longestIncreasingPath(self, matrix) -> int:
        all_nums = []
        if matrix == []:
            return 0
        if matrix == [[]]:
            return 0
        width = len(matrix[0])
        height = len(matrix)
        for y in range(height):
            for x in range(width):
                all_nums.append((y, x, matrix[y][x]))
        # pad 0 as a boundry , therefore we don't need to check
        # if a ny,nx is still inside matrix note x[-1] = x[last]
        matrix.append([0] * width)
        for row in matrix:
            row.append(0)
        # for all position init value is 1
        # saving_matrix[i][j] mean longest path end with matrix[i][j]
        print(matrix)
        saving_matrix = [[1 for _ in range(width)] for _ in range(height)]

        # we need traverse from smallest num as you will never visit
        # a number smller than current position ,
        # i.e: if we have slove 1,2,4,6 in saving_matrix, than they will
        # never be update when you visit number bigger than 6
        all_nums = sorted(all_nums, key=lambda x: x[2], reverse=True)
        print(all_nums)
        while all_nums:
            y, x, num = all_nums.pop()
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ny = y + dy
                nx = x + dx
                if matrix[ny][nx] > num:
                    saving_matrix[ny][nx] = max(saving_matrix[ny][nx], saving_matrix[y][x] + 1)
        print(saving_matrix)
        print(reduce(lambda a, b: a + b, saving_matrix))
        # 这个reduce 是把二维变成一维
        return max(reduce(lambda a, b: a + b, saving_matrix))


nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
s = Solution()
print(s.longestIncreasingPath(matrix=nums))