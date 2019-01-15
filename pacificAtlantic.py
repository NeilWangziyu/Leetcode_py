class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        res = []
        if len(matrix) == 1:
            for i in range(len(matrix[0])):
                res.append([0,i])
            return res

        if len(matrix[0]) == 1:
            for j in range(len(matrix)):
                res.append([j, 0])
            return res


        pacific = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        Atlantic = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        print(pacific)


        def DFS(i, j, Flag):
        #     flag= 1:pacific
            if Flag == 1:
                if pacific[i][j] ==False:
                    pacific[i][j] = True

                    if i > 0:
                        if matrix[i-1][j] >= matrix[i][j]:
                            DFS(i-1, j, Flag)
                    if j > 0:
                        if matrix[i][j-1] >= matrix[i][j]:
                            DFS(i, j-1, Flag)
                    if i< len(matrix)-1:
                        if matrix[i+1][j] >= matrix[i][j]:
                            DFS(i+1, j, Flag)
                    if j< len(matrix[0])-1:
                        if matrix[i][j+1] >= matrix[i][j]:
                            DFS(i, j+1, Flag)

            else:
                if Atlantic[i][j] == False:
                    Atlantic[i][j] = True
                    if i > 0:
                        if matrix[i-1][j] >= matrix[i][j]:
                            DFS(i-1, j, Flag)
                    if j > 0:
                        if matrix[i][j-1] >= matrix[i][j]:
                            DFS(i, j-1, Flag)
                    if i< len(matrix)-1:
                        if matrix[i+1][j] >= matrix[i][j]:
                            DFS(i+1, j, Flag)
                    if j< len(matrix[0])-1:
                        if matrix[i][j+1] >= matrix[i][j]:
                            DFS(i, j+1, Flag)


        for index in range(len(matrix[0])):
            DFS(0, index, 1)
            DFS(len(matrix)-1, index, 0)

        for jex in range(len(matrix)):
            DFS(jex, 0, 1)
            DFS(jex, len(matrix[0])-1, 0)

        print(pacific)
        print(Atlantic)

        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific[i][j] ==True and Atlantic[i][j] == True:
                    res.append([i, j])
        return res

    def pacificAtlantic2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        step = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []
        row = len(matrix)
        col = len(matrix[0])
        q_flag = [[False] * col for _ in range(row)]
        a_flag = [[False] * col for _ in range(row)]

        def dfs(i, j, visited):
            # 走过的标记
            visited[i][j] = True
            for x, y in step:
                tmp_i, tmp_j = i + x, j + y
                # 到边界或已走过或
                if tmp_i < 0 or tmp_j < 0 or tmp_i >= row or tmp_j >= col or matrix[tmp_i][tmp_j] < matrix[i][
                    j] or visited[tmp_i][tmp_j]:
                    continue
                dfs(tmp_i, tmp_j, visited)

        for m in range(row):
            dfs(m, 0, q_flag)
            dfs(m, col - 1, a_flag)
        for n in range(col):
            dfs(0, n, q_flag)
            dfs(row - 1, n, a_flag)
        for i in range(row):
            for j in range(col):
                if q_flag[i][j] and a_flag[i][j]:
                    res.append([i, j])
        return res


matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# matrix = [[1,1],[1,1],[1,1]]

s = Solution()
print(s.pacificAtlantic(matrix))