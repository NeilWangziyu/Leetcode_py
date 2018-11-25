class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0

        row = len(board)
        col = len(board[0])

        count = 0
        # count_board = [[0 for _ in range(row)] for _ in range(col)]
        # print(count_board)
        for i in range(row):
            for j in range(col):
                if board[i][j] == '.':
                    pass
                else:
                    # board[i][j] != '.'
                    if board[i][j] == 'X':
#                         means has not been scaned
                        count += 1
                        board[i][j] = '.'
                    #    先往下找，再往右边找
                        tem_i = i + 1
                        while(tem_i<row and board[tem_i][j] == 'X'):
                            board[tem_i][j] = '.'
                            tem_i += 1

                        tem_j = j + 1
                        while (tem_j < col and board[i][tem_j] == 'X'):
                                board[i][tem_j] = '.'
                                tem_j += 1


        print(board)
        return count






# board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
board = [["X","X","X"]]
s = Solution()
print(s.countBattleships(board))