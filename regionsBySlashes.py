class Solution:
    checked_grid = [[]]
    def regionsBySlashes(self, grid) -> int:
        if not grid:
            return 0

        # print(len(grid[0]))
        row = len(grid)
        col = len(grid[0])

        self.checked_grid = [[0 for _ in range(col * 3)] for _ in range(row * 3)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '\\':
                    self.checked_grid[i * 3][j * 3] = 1
                    self.checked_grid[i * 3 + 1][j * 3 + 1] = 1
                    self.checked_grid[i * 3 + 2][j * 3 + 2] = 1
                elif grid[i][j] == '/':
                    self.checked_grid[i * 3 + 2][j * 3] = 1
                    self.checked_grid[i * 3 + 1][j * 3 + 1] = 1
                    self.checked_grid[i * 3][j * 3 + 2] = 1


        # print(self.checked_grid)

        count = 0
        for i in range(row * 3):
            for j in range(col * 3):
                if self.checked_grid[i][j] == 0:
                    self.BFS(i, j, row)
                    # print(self.checked_grid)
                    count += 1

        # print(self.checked_grid)
        return count

    def BFS(self, it, jt, row):
        # print(it, jt)
        if self.checked_grid[it][jt] == 0:
            self.checked_grid[it][jt] = 1
        if it > 0:
            if self.checked_grid[it - 1][jt] == 0:
                self.BFS(it - 1, jt, row)

        elif jt > 0:
            if self.checked_grid[it][jt - 1] == 0:
                self.BFS(it, jt - 1, row)
        elif it < row - 1:
            if self.checked_grid[it + 1][jt] == 0:
                self.BFS(it + 1, jt, row)
        elif jt < row - 1:
            if self.checked_grid[it][jt + 1] == 0:
                self.BFS(it, jt + 1, row)
        return


# ----------------------------

class Node:
    def __init__(self):
        self.p = self
        self.rank = 0

class Solution1(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        grid_set = []
        for i in range(len(grid)):
            grid_set.append([])
            for j in range(len(grid)):
                grid_set[i].append([Node(), Node(), Node(), Node()])

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i < len(grid)-1:
                    self.union(grid_set[i][j][2], grid_set[i+1][j][0])
                if j < len(grid)-1:
                    self.union(grid_set[i][j][3], grid_set[i][j+1][1])
                if grid[i][j] != "/":
                    self.union(grid_set[i][j][0], grid_set[i][j][3])
                    self.union(grid_set[i][j][1], grid_set[i][j][2])
                if grid[i][j] != "\\":
                    self.union(grid_set[i][j][0], grid_set[i][j][1])
                    self.union(grid_set[i][j][2], grid_set[i][j][3])

        result_set = set()
        for i in range(len(grid)):
            for j in range(len(grid)):
                for k in range(4):
                    result_set.add(self.find_set(grid_set[i][j][k]))

        return len(result_set)

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1

    def find_set(self, x):
        if x.p != x:
            x.p = self.find_set(x.p)
        return x.p


class Solution3:
    def regionsBySlashes(self, grid) -> int:
        size = len(grid)
        # 建立所有格点组成的字典，默认指向自己
        V = {(x, y): (x, y) for y in range(size + 1) for x in range(size + 1)}

        # 所有四边都属于同一个等价类
        for x, y in V:
            if x == 0 or x == size or y == 0 or y == size:
                V[(x, y)] = (0, 0)

        def find(Y, a):
            while Y[a] != a:
                Y[a] = Y[Y[a]]
                a = Y[a]
            return (a)

        counter = 1
        for i in range(size):
            for j in range(size):
                if grid[i][j] == "\\":
                    # 一旦产生了圈，则意味着产生了一个新的面，面数加 1
                    if find(V, (i, j)) == find(V, (i + 1, j + 1)):
                        counter += 1
                    else:
                        V[find(V, (i, j))] = find(V, (i + 1, j + 1))
                elif grid[i][j] == "/":
                    # 一旦产生了圈，则意味着产生了一个新的面，面数加 1
                    if find(V, (i + 1, j)) == find(V, (i, j + 1)):
                        counter += 1
                    else:
                        V[find(V, (i + 1, j))] = find(V, (i, j + 1))
        print(V)
        return counter


if __name__ == "__main__":
    grid = [
      " /",
      "/ "
    ]
    s = Solution()
    s1 = Solution1()
    s3 = Solution3()

    print(s1.regionsBySlashes(grid))
    print(s.regionsBySlashes(grid))
    print(s3.regionsBySlashes(grid))

    grid = [
      "\\/",
      "/\\"
    ]
    print(s1.regionsBySlashes(grid))
    print(s.regionsBySlashes(grid))
    print(s3.regionsBySlashes(grid))

