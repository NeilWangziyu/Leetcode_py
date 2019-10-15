# Definition for a QuadTree node.
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# class Solution:
#     def construct(self, grid):
#         root = Node('*', True, None, None, None, None);
#         if len(grid) == 1:
#             root.isLeaf = True;
#             root.val = True if grid[0][0] == 1 else False;
#             return root
#         if self.allValueSame(grid):  # 所有值相等
#             root.isLeaf = True;
#             root.val = True if grid[0][0] == 1 else False;
#         else:  # 并非所有值相等
#             # halfLength = len(grid) // 2  # 使用 // 表示整除
#             root.isLeaf = False
#             # 如果网格中有值不相等，这个节点就不是叶子节点
#             # 使用array来完成二维数组的切片
#
#             length = len(grid)
#             left_up = []
#             for i in range(length // 2):
#                 tem = []
#                 for j in range(length // 2):
#                     tem.append(grid[i][j])
#                 left_up.append(tem)
#
#             right_up = []
#             for i in range(length // 2, length):
#                 tem = []
#                 for j in range(length // 2):
#                     tem.append(grid[i][j])
#                 right_up.append(tem)
#
#             left_down = []
#             for i in range(length // 2):
#                 tem = []
#                 for j in range(length // 2, length):
#                     tem.append(grid[i][j])
#                 left_down.append(tem)
#
#             right_down = []
#             for i in range(length // 2, length):
#                 tem = []
#                 for j in range(length // 2, length):
#                     tem.append(grid[i][j])
#                 right_down.append(tem)
#
#             root.topLeft = self.construct(left_up)
#             root.topRight = self.construct(right_up)
#             root.bottomLeft = self.construct(left_down)
#             root.bottomRight = self.construct(right_down)
#
#         return root
#
#     def allValueSame(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: boolean
#         """
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[0][0] != grid[i][j]:
#                     return False
#         return True


class Solution:

    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct_core(grid, x, y, lenth):
            check_num = grid[x][y]
            for i in range(x, x + lenth):
                for j in range(y, y + lenth):
                    if check_num != grid[i][j]:
                        isLeaf = False
                        topLeft = construct_core(grid, x, y, lenth // 2)
                        topRight = construct_core(grid, x, y + lenth // 2, lenth // 2)
                        bottomLeft = construct_core(grid, x + lenth // 2, y, lenth // 2)
                        bottomRight = construct_core(grid, x + lenth // 2, y + lenth // 2, lenth // 2)
                        return Node(check_num, isLeaf, topLeft, topRight, bottomLeft, bottomRight)

            isLeaf = True
            return Node(check_num, isLeaf, None, None, None, None)

        # val, isLeaf, topLeft, topRight, bottomLeft, bottomRight

        return construct_core(grid, 0, 0, len(grid))







