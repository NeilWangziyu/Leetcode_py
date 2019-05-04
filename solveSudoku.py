class Solution:
    def solveSudoku(self, board) -> None:
        """
        DFS
        Do not return anything, modify board in-place instead.
        """

        def DFS(board, row_check, col_check, block_check, x, y):
        #     x:row index begins
        #     y:col index begins
            while (board[x][y] != '.'):
                # search empty place
                y += 1
                if y >= 9:
                    x += 1
                    y = 0
                if x >= 9:
                    return True

            for num in range(1, 10):
                block_index = x//3 * 3 + y // 3
                if row_check[x][num] == False and col_check[y][num] == False and block_check[block_index][num] == False:
                    board[x][y] = str(num)
                    row_check[x][num] = True
                    col_check[y][num] = True
                    block_check[block_index][num] = True
                    if DFS(board, row_check, col_check, block_check, x, y):
                        return True
                    else:
                        board[x][y] = "."
                        row_check[x][num] = False
                        col_check[y][num] = False
                        block_check[block_index][num] = False
            return False

        def print_board(board):
            for each in board:
                print(each)

        row_check = [[False for _ in range(10)] for _ in range(9)]
        # index:up to down
        col_check = [[False for _ in range(10)] for _ in range(9)]
        # index:left to right
        block_check = [[False for _ in range(10)] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] != '.'):
                    num = ord(board[i][j]) - ord('0')
                    # print(num)
                    row_check[i][num] = True
                    col_check[j][num] = True
                    # blockIndex = i / 3 * 3 + j / 3，取整
                    block_check[i // 3 * 3 + j // 3][num] = True
        #
        # print(row_check)
        # print(col_check)
        # print(block_check)
        DFS(board, row_check, col_check, block_check, 0, 0)
        print_board(board)

    # -----------------------------------------------------------------------------

    def solveSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 首先遍历一遍数独，把每个空格可以填入的数字都保存下来
        rows_list = dict()
        cols_list = dict()
        rect_list = dict()
        judge_dict = dict()
        # 首先把已经有的数字都放入对应的字典中，用字符串拼接的形式，方便后面查找
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] != '.':
                    if row_idx not in rows_list:
                        rows_list[row_idx] = board[row_idx][col_idx]
                    else:
                        rows_list[row_idx] += board[row_idx][col_idx]
                    if col_idx not in cols_list:
                        cols_list[col_idx] = board[row_idx][col_idx]
                    else:
                        cols_list[col_idx] += board[row_idx][col_idx]
                    if (row_idx // 3, col_idx // 3) not in rect_list:
                        rect_list[row_idx // 3, col_idx // 3] = board[row_idx][col_idx]
                    else:
                        rect_list[row_idx // 3, col_idx // 3] += board[row_idx][col_idx]
                else:
                    if row_idx not in rows_list:
                        rows_list[row_idx] = ''
                    if col_idx not in cols_list:
                        cols_list[col_idx] = ''
                    if (row_idx // 3, col_idx // 3) not in rect_list:
                        rect_list[row_idx // 3, col_idx // 3] = ''

        # 然后再遍历一次，新建一个字典，用来存放每个格子可以选择的有效数字
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == '.':
                    judge_dict[row_idx, col_idx] = [n for n in '123456789' if n not in (
                                rows_list[row_idx] + cols_list[col_idx] + rect_list[row_idx // 3, col_idx // 3])]

        # 开始遍历，往里面填充新的数字，采用递归的方式
        # 从第一个格子开始遍历
        # 九宫格一共是9*9=81个格子，此处将二维数组变成一维数组，方便遍历
        _ = self.search_answer(board, judge_dict, False)
        return None

    def identify(self, str_num, row_idx, col_idx, store_dict, judge_dict, board):
        # 添加到board里面
        board[row_idx][col_idx] = str_num
        # 然后再judge_dict里面将该位置的key删掉，表明这个位置已经固定
        judge_dict.pop((row_idx, col_idx))
        # 然后删去有关联因素的行、列、小方块的judge_dict里面的相关value值。
        for r, c in judge_dict:
            if (r == row_idx or c == col_idx or (row_idx // 3, col_idx // 3) == (r // 3, c // 3)) and str_num in \
                    judge_dict[r, c]:
                # 删除之前先保存到store_dict里面
                store_dict[r, c] = str_num
                # 删除相关联的judge_dict
                judge_dict[r, c].remove(str_num)
                if len(judge_dict[r, c]) == 0:
                    return False
        return True

    def rollback_data(self, row_idx, col_idx, store_dict, judge_dict, board):
        # 说明这次尝试不对，于是恢复judge_dict和board
        board[row_idx][col_idx] = '.'
        for key in store_dict:
            if key in judge_dict:
                judge_dict[key].extend(store_dict[key])
            else:
                judge_dict[key] = store_dict[key]
        return None

    def search_answer(self, board, judge_dict, return_flag):
        if len(judge_dict) == 0:
            # 说明judge_dict已经用完，数独已经解出，可以返回了
            return True
        # 寻找长度最短的judge_dict
        (row_idx, col_idx) = min(judge_dict, key=lambda x: len(judge_dict[x]))
        # 这句话很精髓啊！！！！！min的第一个函数就是一个可遍历对象， lambda的输入就是第一个参数里面的每一个值（key）
        for str_num in judge_dict[row_idx, col_idx]:
            # 将这个位置的judge_dict的可选值单独存一个字典store_dict
            store_dict = {(row_idx, col_idx): judge_dict[row_idx, col_idx]}
            tmp_return_flag = self.identify(str_num, row_idx, col_idx, store_dict, judge_dict, board)
            if tmp_return_flag is True:
                # 完成之后递归调用函数，进行下一步
                return_flag = self.search_answer(board, judge_dict, return_flag)
                if return_flag is True:
                    return return_flag

            # 回退judge_dict和board
            self.rollback_data(row_idx, col_idx, store_dict, judge_dict, board)

        return False


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

s = Solution()
print(s.solveSudoku(board))
