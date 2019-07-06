class Edges:
    def __init__(self, s, e, w):
        self.s = s
        self.e = e
        self.w = w

    def __lt__(self, other):
        return  self.w < other.w

    def __eq__(self, other):
        return self.w == other.w

    def __repr__(self):
        return str(self.s)+'-'+str(self.e)+"({})".format(self.w)


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        mat = {}
        for i in range(N):
            mat[i] = []
        for each in times:
            mat[each[0]-1].append(Edges(each[0]-1, each[1]-1, each[2]))

        marker = [False for _ in range(N)]
        MinPQ = []
        for each in mat[K-1]:
            MinPQ.append(each)
        marker[K-1] = True
        MinPQ.sort()
        mst = []

        count = 0

        while(MinPQ):
            this_edge = MinPQ.pop(0)
            end = this_edge.e
            if marker[end]:
                continue
            else:
                marker[end] = True
                mst.append(this_edge)
                count += this_edge.w
                for all in MinPQ:
                    all.w = max(0, all.w-this_edge.w)
                for each in mat[end]:
                    MinPQ.append(each)
                MinPQ.sort()


        if not False in marker:
            return count
        else:
            return -1

    def networkDelayTime2(self, times, N, k):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
该题用到了Dijkstra算法求最短路径。可以计算出从一个点，到所有点的距离。
        利用的都是邻接矩阵进行求解
        """
        import collections
        nodes = collections.defaultdict(dict)
        Q = set(range(N))

        for u,v,w in times:
            nodes[u-1][v-1] = w
        print(nodes)
        dist = [float('inf')]*N
        dist[k-1] = 0


        while Q:
            u = min(Q, key = lambda x: dist[x])#可以学习
            Q.remove(u)
            for v in nodes[u]:#和这个点连接的所有点
                temp = dist[u]+nodes[u][v]
                if dist[v] > temp:
                    dist[v] = temp
        d = max(dist)
        return -1 if d==float('inf') else d


times = [[1,2,1],[2,3,2],[1,3,4]]
N = 3
K = 1

s = Solution()
print(s.networkDelayTime2(times, N, K))