class Solution:
    def removeStones(self, stones) -> int:
        checked_list = [False for _ in range(len(stones))]
        count = 0
        def DFS(index, cx, cy):
            checked_list[index] = True
            for i in range(len(stones)):
                if checked_list[i] == False:
                    if (stones[i][0] == cx or stones[i][1] == cy):
                        checked_list[index] = True
                        DFS(i, stones[i][0], stones[i][1])

        for num in range(len(stones)):
            if not checked_list[num]:
                DFS(num, stones[num][0], stones[num][1])
                count += 1
        return len(stones) - count

    def removeStones2(self, stones) -> int:
        from collections import defaultdict
        # 比如default(int)
        # 则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key, d[key]
        # 也有一个默认值，这个默认值是int()
        # 的默认值0.

        stones = list(map(tuple, stones))
        graph = {x: x for x in stones}
        print(graph)

        def find(g, x):
            while g[x] != x:
                g[x] = g[g[x]]
                x = g[x]
            return (x)

        for i in range(len(stones) - 1):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    if find(graph, stones[i]) != find(graph, stones[j]):
                        graph[find(graph, stones[i])] = find(graph, stones[j])

        con_comp = defaultdict(int)

        for x in stones:
            con_comp[find(graph, x)] += 1
        print(con_comp)
        return (sum([i - 1 for i in con_comp.values()]))

    def removeStones3(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """

        p = list(range(len(stones)))
        # 老大的字典
        x = {}
        y = {}

        def find(s):
            if p[s] != s:
                s = find(p[s])
            return s

        for i, stone in enumerate(stones):
            if stone[0] not in x:  # 如果不在x这个字典里,说明这是这个x值的第一个,是老大
                x[stone[0]] = i
            else:
                p[i] = x[stone[0]]  # 再遇到重复这个x值的,都是那个老大的小弟

        # [0,0,2,2,3,3,6]
        for i, stone in enumerate(stones):
            if stone[1] not in y:
                y[stone[1]] = i
            else:
                p[find(i)] = find(y[stone[1]])

        return len(p) - len([i for i in range(len(p)) if i == p[i]])


if __name__ == "__main__":
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    s = Solution()
    print(s.removeStones(stones))
    print(s.removeStones2(stones))