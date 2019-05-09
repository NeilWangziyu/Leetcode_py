class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # NxN 的国际象棋棋盘
        # “骑士”位于 (r, c)
        # 并打算进行 K 次移动
        memory = {}
        moves = ((-1, -2), (-2, -1),(-2, 1), (-1, 2),(1, -2), (2, -1),(2, 1), (1, 2))
        # print(moves[0][0])

        def DFS(K, r, c):
            if r < 0 or c < 0 or r >=N or c>=N:
                return 0
            if  K == 0:
                return 1
            if (K, r, c) in memory:
                return memory[(K, r, c)]
            p = 0
            for move in moves:
                p += DFS(K-1, r+move[0], c+move[1])
            p /= 8
            memory[(K, r, c)] = p
            return p
        # print(memory)
        return DFS(K, r, c)

    def knightProbability2(self, n: 'int', k: 'int', x: 'int', y: 'int') -> 'float':
        if not k:
            return 1.0
        if not n or n <= 1:
            return 0.0

        m = n + 1 >> 1
        pre = [[1] * m for _ in range(m)]
        cur = [[0] * m for _ in range(m)]

        delta = (
            (-1, -2), (1, -2),
            (-1, 2), (1, 2),
            (-2, -1), (2, -1),
            (-2, 1), (2, 1),
        )

        def prob(i, j):
            if not (0 <= i < n and 0 <= j < n):
                return 0
            if i << 1 >= n:
                i = n - 1 - i
            if j << 1 >= n:
                j = n - 1 - j

            return pre[i][j] if i < j else pre[j][i]

        for _ in range(k - 1):
            for i in range(m):
                for j in range(i, m):
                    cur[i][j] = sum(prob(i + di, j + dj) for di, dj in delta) / 8.0

            pre, cur = cur, pre

        return sum(prob(x + di, y + dj) for di, dj in delta) / 8.0


s = Solution()
print(s.knightProbability(10, 10, 0, 0))