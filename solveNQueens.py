class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def conflict(state, nextX):
            # 冲突检查，在定义state时，采用state来标志每个皇后的位置，其中索引用来表示横坐标，基对应的值表示纵坐标，
            # 例如： state[0]=3，表示该皇后位于第1行的第4列上

            nextY = len(state)
            for i in range(nextY):
                # 如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
                if abs(state[i] - nextX) in (0, nextY - i):
                    return True
            return False

        def queens(num, state=()):
            # 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
            for pos in range(num):
                if not conflict(state, pos):
                    if len(state) == num - 1:
                        yield (pos,)
                    else:
                        for result in queens(num, state + (pos,)):
                            yield (pos,) + result

        def prettyprint(solution):
            res_list = []

            def line(pos, length=len(solution)):
                return '.' * (pos) + 'Q' + '.' * (length - pos - 1)

            for pos in solution:
                res_list.append(line(pos))

        result = list(queens(n))
        print(result)
        return (prettyprint(result))



# -----------------------------------------
# 第二种方法
# -----------------------------------------

    def make(self, mark):
        r = [['.' for _ in range(len(mark))] for _ in range(len(mark))]
        for i in mark:
            r[i][mark[i]] = 'Q'
        for k, v in enumerate(r):
            r[k] = ''.join(v)
        return r

    def recursive(self, mark, cur, ret):

        if cur == len(mark):
            ret.append(self.make(mark))
            return

        for i in range(len(mark)):
            mark[cur], down = i, True
            for j in range(cur):
                if mark[j] == i or abs(i - mark[j]) == cur - j:
                    down = False
                    break
            if down:
                self.recursive(mark, cur + 1, ret)

    def solveNQueens2(self, n):

        ret = []
        self.recursive([None] * n, 0, ret)
        return ret

# -----------------------------------------
# 第三种方法
# -----------------------------------------

    def solveNQueens3(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res, y_stack, x_minus_y_stack, x_plus_y_stack = [], [], [], []

        def dfs(x=0):
            if x == n:
                res.append(['.' * y + 'Q' + '.' * (n - 1 - y) for y in y_stack])
                return
            for y in range(n):
                if (y not in y_stack) and (x - y not in x_minus_y_stack) and (x + y not in x_plus_y_stack):
                    y_stack.append(y)
                    x_minus_y_stack.append(x - y)
                    x_plus_y_stack.append(x + y)
                    dfs(x + 1)  # increasing depth
                    y_stack.pop()
                    x_minus_y_stack.pop()
                    x_plus_y_stack.pop()

        dfs()  # default is x = 0
        return res
