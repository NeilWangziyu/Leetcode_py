from typing import List


class weightedEdge():
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

class EdgeWeightedGraph():
    def __init__(self, V, Edges):
        self.V = V
        self.E = 0
        self.mat = {}
        for i in range(V):
            self.mat[i] = []
        if Edges:
            for each in Edges:
                self.addEdge(each[0]-1, each[1]-1, each[2])

    def addEdge(self, start, end, weight):
        if start not in self.mat or end not in self.mat:
            raise ValueError("start or end not in this graph")
        else:
            self.mat[start].insert(0, weightedEdge(start, end, weight))
            self.mat[end].insert(0,weightedEdge(end, start, weight))
            self.E += 1

    def PrimMST_weight(self):
        #         最小生成树
        #         marker and mst is replaced by edgeTo and distTo
        # if len(self.Search_BFS(0)) != self.V:
        #     raise ValueError("it is not a connected graph")

        marker = [False for _ in range(self.V)]
        distTo = [float('inf') for _ in range(self.V)]
        pq = []
        mst = [None for _ in range(self.V)]
        # pq:优先队列
        distTo[0] = 0
        marker[0] = True
        for each in self.mat[0]:
            pq.append(each)
        pq.sort(reverse=False)

        while (pq):
            check_edge = pq.pop(0)
            marker[check_edge.end] = True
            if distTo[check_edge.end] > check_edge.weight:
                distTo[check_edge.end] = check_edge.weight
                mst[check_edge.end] = check_edge

            for each in self.mat[check_edge.end]:
                if marker[each.end] == False:
                    pq.append(each)
            pq.sort()

        res = sum(distTo)
        if res == float("inf"):
            return -1
        else:
            return res


class Solution:
    def minimumCost(self, N: int, conections: List[List[int]]) -> int:
        matrix = {}
        for i in range(N):
            matrix[i] = []
        for each in conections:
            matrix[each[0]-1].append([each[1]-1, each[2]])
            matrix[each[1] - 1].append([each[0] - 1, each[2]])

        marker = [False for _ in range(N)]

        distTo = [float('inf') for _ in range(N)]
        pq = []

        # pq:优先队列
        distTo[0] = 0
        marker[0] = True
        for each in matrix[0]:
            pq.append(each)
        pq.sort(reverse=False, key=lambda x:x[0])

        while(pq):
            check_edge = pq.pop(0)
            marker[check_edge[0]] = True
            if distTo[check_edge[0]] > check_edge[1]:
                distTo[check_edge[0]] = check_edge[1]

            for each in matrix[check_edge[0]]:
                if marker[each[0]] == False:
                    pq.append(each)
            pq.sort(reverse=False, key=lambda x:x[0])


        res = sum(distTo)
        if res == float("inf"):
            return -1
        else:
            return res
    # -----------------------

    def minimumCost2(self, N: int, conections: List[List[int]]) -> int:

        # 这个还不如第一种快

        G = EdgeWeightedGraph(N, conections)
        return G.PrimMST_weight()


    # -----------------------
    def minimumCost3(self, N: int, conections: List[List[int]]) -> int:
        def find(i):
            if father[i] == i:
                return i
            else:
                father[i] = find(father[i])
                return father[i]

        conn = sorted(conections, key=lambda item: item[2])
        visited = []
        res = 0
        father = [i for i in range(N + 1)]
        for item in conn:
            i, j = item[0], item[1]
            cost = item[2]
            fi, fj = find(i), find(j)
            if fi == fj:
                continue
            res += cost
            father[fi] = fj
            visited.append((i, j))
        return res if len(visited) == N - 1 else -1


s = Solution()
N = 3
conections = [[1,2,5],[1,3,6],[2,3,1]]

print(s.minimumCost(N, conections))
print(s.minimumCost2(N, conections))

N = 4
conections = [[1,2,3],[3,4,4]]
print(s.minimumCost(N, conections))
print(s.minimumCost2(N, conections))

