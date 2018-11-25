class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        本题应该从下往上，从右往左进行分析
        """
        width = len(dungeon)
        length = len(dungeon[0])

        if length == 1 and width == 1:
            if dungeon[length - 1][width - 1] < 0:
                return 1 - dungeon[length - 1][width - 1]
            else:
                return 1

        new_map = []
        for i in range(width):
            row = []
            for j in range(length):
                row.append(0)
            new_map.append(row)
        new_map[-1][-1] = dungeon[-1][-1]

        for i in range(2, width + 1):
            print(i)
            if new_map[-i + 1][-1] + dungeon[-i][-1] < 0:
                new_map[-i][-1] = new_map[-i + 1][-1] + dungeon[-i][-1]
            else:
                new_map[-i][-1] = 0

        for i in range(2, length + 1):
            print(i)
            if new_map[-1][-i + 1] + dungeon[-1][-i] < 0:
                new_map[-1][-i] = new_map[-1][-i + 1] + dungeon[-1][-i]
            else:
                new_map[-1][-i] = 0

        for i in range(2, width + 1):
            for j in range(2, length + 1):
                left = new_map[-i + 1][-j] + dungeon[-i][-j]
                if left > 0:
                    left = 0

                godown = new_map[-i][-j + 1] + dungeon[-i][-j]
                if godown > 0:
                    godown = 0

                new_map[-i][-j] = max(left, godown)

        print(new_map)
        return -new_map[0][0] + 1

        # new_map = []
        # for i in range(length):
        #     row = []
        #     for j in range(width):
        #         row.append([0, 0])
        #     new_map.append(row)
        #
        # new_map[0][0][0] = dungeon[0][0]
        # new_map[0][0][1] = dungeon[0][0]
        #
        # for i in range(1, length):
        #     new_map[i][0][0] = min(new_map[i - 1][0][0], new_map[i - 1][0][1] + dungeon[i][0])
        #     new_map[i][0][1] = new_map[i - 1][0][1] + dungeon[i][0]
        #
        # for j in range(1, width):
        #     new_map[0][j][0] = min(new_map[0][j - 1][0], new_map[0][j - 1][1] + dungeon[0][j])
        #     new_map[0][j][1] = new_map[0][j - 1][1] + dungeon[0][j]
        #
        # for i in range(1, length):
        #     for j in range(1, width):
        #         if min(new_map[i - 1][j][0], new_map[i - 1][j][1] + dungeon[i][j]) > min(new_map[i][j - 1][0],
        #                                                                                  new_map[i][j - 1][1] +
        #                                                                                  dungeon[i][j]):
        #
        #         # if new_map[i - 1][j][1] + dungeon[i][j]>new_map[i][j - 1][1] + dungeon[i][j]:
        #
        #             #             从上面下来
        #             new_map[i][j][0] = min(new_map[i - 1][j][0], new_map[i - 1][j][1] + dungeon[i][j])
        #             new_map[i][j][1] = new_map[i - 1][j][1] + dungeon[i][j]
        #
        #
        #         else:
        #             # 从左边来
        #             new_map[i][j][0] = min(new_map[i][j - 1][0], new_map[i][j - 1][1] + dungeon[i][j])
        #             new_map[i][j][1] = new_map[i][j - 1][1] + dungeon[i][j]
        #
        # print(new_map)
        # print(new_map[length - 1][width - 1][0])
        # mini_costHP = new_map[length - 1][width - 1][0]
        # if mini_costHP < 0:
        #     return 1 - new_map[length - 1][width - 1][0]
        # else:
        #     return 1


s = Solution()
dungeon = [[-2,-3,3]]
print(s.calculateMinimumHP(dungeon))