class Solution:
    def DFS(self, i, j, board):
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != 'O':
            return

        board[i][j] = '-'
        for each in self.pos:
            self.DFS(i + each[0], j + each[1], board)
        return

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        self.pos = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        row = len(board)
        col = len(board[0])

        for i in range(col):
            if board[0][i] == 'O':
                self.DFS(0, i, board)
            if board[row - 1][i] == 'O':
                self.DFS(row - 1, i, board)
        for j in range(1, row - 1):
            if board[j][0] == 'O':
                self.DFS(j, 0, board)
            if board[j][col - 1] == 'O':
                self.DFS(j, col - 1, board)

        pos = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        row = len(board)
        col = len(board[0])

        for i in range(col):
            self.DFS(0, i, board)
            self.DFS(row - 1, i, board)

        for j in range(1, row - 1):
            self.DFS(j, 0, board)
            self.DFS(j, col - 1, board)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'

