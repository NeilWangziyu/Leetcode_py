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

        for i in range(row):
            for j in range(col):
                if board[i][j] == '.':
                    pass
                else:
                    if board[i][j] == 'X':
                        count += 1
                        board[i][j] = '.'
                        tem_i = i + 1
                        while (tem_i < row and board[tem_i][j] == 'X'):
                            board[tem_i][j] = '.'
                            tem_i += 1

                        tem_j = j + 1
                        while (tem_j < col and board[i][tem_j] == 'X'):
                            board[i][tem_j] = '.'
                            tem_j += 1
        return count



    def countBattleships2(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if 'X' == board[i][j] and (0 == i or '.' == board[i - 1][j]) and (0 == j or '.' == board[i][j - 1]):
                    count += 1
        return count


board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

board2 = [["X","X","X"]]

s = Solution()
print(s.countBattleships(board))
print(s.countBattleships2(board))

print(s.countBattleships(board2))
print(s.countBattleships2(board2))