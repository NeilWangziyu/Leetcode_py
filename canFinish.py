class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        very important
        """
        def dp(grap, index, visit, canf):
        #     深度优先搜索
            visit.append(index)
            if canf[index] == 1:
        #         如果该门课已经被判定过，返回正
                return True
            for i in range(numCourses):#对该门课的每一个先决条件进行判断
                if grap[index][i] == 1:
                    if i in visit:
                        # i 在visit里面，说明其已经被访问过，出现环，false
                        return False
                    if not dp(grap, i, visit[:], canf):
                        # 这里的visit[:]和之前的visit没有关系，其值和visit一样，但是之后对其的修改和visit没关系，体现回退
                        return False
                    else:
                        canf[i] = 1
            return True

        grap = [[0] * numCourses for _ in range(numCourses)]
        for line in prerequisites:
            grap[line[0]][line[1]] = 1
        canf = [-1] * numCourses
        for i in range(numCourses):
            if canf[i] == 1:
                continue
            if not dp(grap, i, [], canf):
                return False
            else:
                canf[i] = 1
        return True


    def canFinish2(self, numCourses, prerequisites):
        edge_graph = [[] for _ in range(numCourses)]
        flag_nfs = [0 for _ in range(numCourses)]
        # flag_nfs=0：没有判断，flag_nfs=1:可以完成，-1：其存在一个点，不行

        for i, j in prerequisites:
            edge_graph[i].append(j)

        print(edge_graph)
        # edge_graph[i]表示i需要多少个先决条件

        def dfs(i):
            if flag_nfs[i] == -1:
                return False
            if flag_nfs[i] == 1:
                return True
            flag_nfs[i] = -1

            for j in edge_graph[i]:
                if not dfs(j):
                    return False

            flag_nfs[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


    def canFinish3(self, numCourses, prerequisites):
        # AOV网络经典算法：
        # must remember
        ind = [[] for _ in range(numCourses)]  # indegree:nx[]矩阵
        oud = [0] * numCourses  # outdegree：n矩阵，out[i]:第i个点可以通过多少课作为条件

        for p in prerequisites:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])

        print(oud)
        print(ind)

        dq = []
        for i in range(numCourses):
            if oud[i] == 0:
                dq.append(i)
        #         dp先加入indegree=0的值

        k = 0
        while dq:
            x = dq.pop(0)
            k += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    dq.append(i)
        #     一次dq，从0开始，把能走完的都走过一遍
        return k == numCourses


numCourses = 5
prerequisites = [[0,1],[0,2],[1,2],[3,0],[4,3],[4,1]]

s = Solution()
print(s.canFinish3(numCourses, prerequisites))