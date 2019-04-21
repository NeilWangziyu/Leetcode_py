class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        if R == 0 and C == 0:
            return [[0, 0]]
        check_grid = [[False for _ in range(C)] for _ in range(R)]
        res = []
        stack = []
        stack.append([r0, c0])
        while(stack):
            check_this = stack.pop(0)
            if check_grid[check_this[0]][check_this[1]]==False:
                check_grid[check_this[0]][check_this[1]] = True
                res.append(check_this)
                if check_this[0] > 0:
                    stack.append([check_this[0]-1, check_this[1]])
                if check_this[1] > 0:
                    stack.append([check_this[0], check_this[1]-1])
                if check_this[0] < R-1:
                    stack.append([check_this[0]+1, check_this[1]])
                if check_this[1] < C - 1:
                    stack.append([check_this[0], check_this[1]+1])
        return res



R = 2
C = 2
r0 = 0
c0 = 1
s = Solution()
print(s.allCellsDistOrder(R, C, r0, c0))

R = 2
C = 3
r0 = 1
c0 = 2
print(s.allCellsDistOrder(R, C, r0, c0))
