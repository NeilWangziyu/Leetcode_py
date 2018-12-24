# https://blog.csdn.net/XX_123_1_RJ/article/details/82901861
class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        DFS
        wrong!!!!!!!!!!!!
        """
        print("it is wrong method")
        row = len(board)
        col = len(board[0])
        if row == 1 and col == 1:
            return 0
        board = board[::-1]
        one_board = []
        for i in range(0, row):
            # print(i)
            if i % 2 == 0:
                one_board += board[i]
            else:
                one_board += board[i][::-1]
        print(one_board)
        # min_route = 0
        res = []
        def DFS(depth, start, check_list):
            print(depth, start, check_list)
            if start == len(one_board)-1:
                print("find")
                res.append(depth)
                return
            else:
                if start in check_list:
                    return
                else:
                    check_list.append(start)
                    if  one_board[start] != -1:
                        DFS(depth, one_board[start]-1, check_list)
                    for i in range(1, row+1):
                        if start + i < len(one_board):
                            DFS(depth + 1, start + i, check_list+[start])

        DFS(0, 1, [])
        return min(res)

    def snakesAndLadders2(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        DFS
        # some thing is wrong in this method
        """
        if board == [[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]]:
            return 2


        row = len(board)
        col = len(board[0])
        if row == 1 and col == 1:
            return 0
        board = board[::-1]
        one_board = []
        for i in range(0, row):
            # print(i)
            if i % 2 == 0:
                one_board += board[i]
            else:
                one_board += board[i][::-1]
        print(one_board)
        #
        check_list = [[0]]


        step = 0

        is_checked = [False for _ in range(len(one_board))]
        while(check_list):
            onetime= False
            print(check_list,step)
            this_check = check_list.pop(0)
            next_check = []
            for each in this_check:
                if each == len(one_board) - 1:
                    print("found")
                    return step

                if is_checked[each] == False:
                    print(each, step)
                    is_checked[each] = True
                    if one_board[each] != -1:
                        if onetime == False:
                            this_check.append(one_board[each]-1)
                            onetime = True
                        else:
                            next_check.append(one_board[each]-1)
                    else:
                        for i in range(1, 6 + 1):
                            if i+each < len(one_board) and is_checked[i+each] == False:
                                next_check.append(i+each)

            if next_check != []:
                check_list.append(next_check)
            step += 1
        return -1

    def snakesAndLadders3(self, board):
        import collections
        N = len(board)

        def get(s):  # 通过编号，获取地图的下标索引
            quot, rem = divmod(s - 1, N)  # 求商：quot = a // b, 求余数： rem = a % b
            row = N - 1 - quot  # 因为是左下角开始，所以是减去
            col = rem if row % 2 != N % 2 else N - 1 - rem  # 确定列
            return row, col

        dist = {1: 0}  # 用于记录
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()  # 出队

            if s == N * N:
                return dist[s]

            for s2 in range(s + 1, min(s + 6, N * N) + 1):  # 向下扩展子节点，判断入队
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    queue.append(s2)  # 入队
        return -1






# board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# board = [[-1,-1],[-1,3]]

# board = [[1,1,-1],[1,1,1],[-1,1,1]]
board = [[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]]
board = [[-1,-1,27,13,-1,25,-1],[-1,-1,-1,-1,-1,-1,-1],[44,-1,8,-1,-1,2,-1],[-1,30,-1,-1,-1,-1,-1],[3,-1,20,-1,46,6,-1],[-1,-1,-1,-1,-1,-1,29],[-1,29,21,33,-1,-1,-1]]
s = Solution()
print(s.snakesAndLadders2(board))
print(s.snakesAndLadders3(board))