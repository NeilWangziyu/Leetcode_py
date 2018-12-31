class Solution:

    def shortestBridge(self, A):
        """
        DFS+BSF,没有做出来
        诶

        :type A: List[List[int]]
        :rtype: int
        """
        check_list = [[False for _ in range(len(A[0]))] for _ in range(len(A))]

        def DFS_land(i, j):
            queue = [[i, j]]
            find_that_land = []
            find_that_sea = []
            while(queue):
                check_that = queue.pop(0)
                if check_list[check_that[0]][check_that[1]] == False:
                    print(check_that[0],check_that[1])
                    if A[check_that[0]][check_that[1]] == 1:
                        check_list[check_that[0]][check_that[1]] = 1
                        find_that_land.append([check_that[0], check_that[1]])
                        if check_that[0]>0:
                            queue.append([check_that[0]-1, check_that[1]])
                        if check_that[0] < len(A[0])-1:
                            queue.append([check_that[0]+ 1, check_that[1]])
                        if check_that[1]> 0:
                            queue.append([check_that[0], check_that[1]-1])
                        if check_that[1] < len(A)-1:
                            queue.append([check_that[0], check_that[1]+1])
                    else:
                        check_list[check_that[0]][check_that[1]] = 0
                        find_that_sea.append([check_that[0],check_that[1]])

            return find_that_land, find_that_sea

        # def BFS()

        print("Sea",DFS_land(0,0)[1])
        print("land",DFS_land(0,0)[0])
        print(check_list)


    def shortestBridge2(self, A):
        import collections
        """
        :type A: List[List[int]]
        :rtype: int
        """
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * N for _ in range(M)]
        hasfind = False
        que = collections.deque()
        for i in range(M):
            if hasfind: break
            for j in range(N):
                if A[i][j] == 1:
                    self.dfs(A, i, j, visited, que)
                    hasfind = True
                    break
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < M and 0 <= y < N:
                        visited[x][y] = 1
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            que.append((x, y))
                        else:
                            continue
            step += 1
        return -1

    def dfs(self, A, i, j, visited, que):
        if visited[i][j]: return
        visited[i][j] = 1
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if A[i][j] == 1:
            que.append((i, j))
            A[i][j] = 2
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if 0 <= x < M and 0 <= y < N:
                    self.dfs(A, x, y, visited, que)
    #
    # ---------------------
    # 作者：负雪明烛
    # 原文：https: // blog.csdn.net / fuxuemingzhu / article / details / 83716820



A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
s = Solution()
print(s.shortestBridge2(A))