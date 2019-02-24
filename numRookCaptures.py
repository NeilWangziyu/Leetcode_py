class Solution:
    def numRookCaptures(self, board: 'List[List[str]]') -> 'int':

        def check(init_i, init_j):
            count = 0
            for tem_j in range(init_j, 8):
                if board[init_i][tem_j] == 'B':
                    break
                if board[init_i][tem_j] == 'p':
                    print("!")
                    count += 1
                    break
            for tem_j in range(init_j, -1, -1):
                if board[init_i][tem_j] == 'B':
                    break
                if board[init_i][tem_j] == 'p':
                    print(init_i, tem_j)
                    count += 1
                    break

            for tem_i in range(init_i, 8):
                if board[tem_i][init_j] == 'B':
                    break
                if board[tem_i][init_j] == 'p':
                    count += 1
                    break

            for tem_i in range(init_i, -1, -1):
                if board[tem_i][init_j] == 'B':
                    break
                if board[tem_i][init_j] == 'p':
                    count += 1
                    break
            return count

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    print(i, j)

                    return check(i,j)
        return 0



board =[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
s = Solution()
print(s.numRookCaptures(board))