class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def test(list):
            tem = set()
            for each_num in list:
                if each_num != '.':
                    if each_num in tem:
                        return False
                    else:
                        tem.add(each_num)
            return True




        list_one = []
        list_two = []
        list_three = []
        col = [[] for _ in range(9)]

        for index, each in enumerate(board):
            if test(each):
                list_one = list_one + each[0:3]
                list_two = list_two + each[3:6]
                list_three = list_three + each[6:9]
                for i in range(len(each)):
                    col[i].append(each[i])

            else:
                return False

            if (index+1) % 3 ==0:
                print(list_one, list_two, list_three)
                if test(list_one) and test(list_two) and test(list_three):
                    list_one = []
                    list_two = []
                    list_three = []
                else:
                    return False


        for each in col:
            if not test(each):
                return False
        return True








board = [[".","2",".",".",".",".",".",".","."],
         [".",".",".",".",".",".","5",".","1"],
         [".",".",".",".",".",".","8","1","3"],
         ["4",".","9",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],[".",".","2",".",".",".",".",".","."],["7",".","6",".",".",".",".",".","."],["9",".",".",".",".","4",".",".","."],[".",".",".",".",".",".",".",".","."]]


board1=[[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]

s = Solution()
print(s.isValidSudoku(board))
# print(s.isValidSudoku(board1))