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


class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        pass
        # matrix = {}
        # for i in range(N):
        #     matrix[i] = []
        # for each in relations:
        #     matrix[each[0]-1].append(each[1]-1)
        #
        # def DFS_circle(index):
        #     onStack[index] = True
        #     marked[index] = True
        #     print(index, onStack, marked)
        #     for w in matrix[index]:
        #         if onStack[w]:
        #             res_Tem = []
        #             x = index
        #             while (x != w):
        #                 res_Tem.append(x)
        #                 x = edgeTo[x]
        #             res_Tem.append(w)
        #             res_Tem.append(index)
        #             cycle.append(res_Tem)
        #         else:
        #             edgeTo[w] = index
        #             DFS_circle(w)
        #         onStack[index] = False
        #
        #
        # marked = [False for _ in range(N)]
        # edgeTo = [-1 for _ in range(N)]
        # cycle = []
        # onStack = [False for _ in range(N)]
        #
        # for i in range(N):
        #     if marked[i] == False:
        #         print(i)
        #         DFS_circle(i)
        #
        # if len(cycle)==0:
        #     return -1
        #
        # reversePost = []  # stack
        # marked = [False for _ in range(N)]
        #
        # def DFS_firstOrder(v):
        #     marked[v] = True
        #     for each_edge in matrix[v]:
        #         w = each_edge[0]
        #         if marked[w] == False:
        #             DFS_firstOrder(w)
        #     reversePost.insert(0, v)
        #
        # for index in range(N):
        #     if marked[index] == False:
        #         DFS_firstOrder(index)
        # # top
        # print(reversePost)







s = Solution()

N = 3
relations = [[1,3],[2,3]]

print(s.minimumSemesters(N, relations))

N = 3
relations = [[1,2],[2,3],[3,1]]
print(s.minimumSemesters(N, relations))
