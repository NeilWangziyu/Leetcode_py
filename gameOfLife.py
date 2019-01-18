class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """


        new_board = [[False for _ in range(len(board[0]))] for  _ in range(len(board))]
        # print(new_board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                count_live = 0
                row_small = max(0, i-1)
                row_larger = min(len(board)-1, i+1)
                col_small = max(0, j-1)
                col_larger = min(len(board[0])-1, j+1)

                for i_t in range(row_small, row_larger+1):
                    for j_t in range(col_small, col_larger+1):
                        if not(i_t==i and j_t == j):
                            print(i_t, j_t)
                            if board[i_t][j_t] == 1:
                                count_live += 1

                # print(i, j, count_live )
                if board[i][j] == 1:
                    if count_live < 2 or count_live>3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
                elif board[i][j]== 0:
                    if count_live == 3:
                        new_board[i][j] = 1
                    else:
                        new_board[i][j]= 0

        # board =  new_board
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = new_board[i][j]


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s = Solution()
s.gameOfLife(board)
print(board)