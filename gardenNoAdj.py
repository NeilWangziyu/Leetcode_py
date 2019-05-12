class Solution:
    def gardenNoAdj(self, N: int, paths):
        if N == 0:
            return []

        if not paths:
            return [1] * N

        next_dict = {}
        for each in paths:
            if each[0] not in next_dict:
                next_dict[each[0]] = [each[1]]
            else:
                next_dict[each[0]].append(each[1])

            if each[1] not in next_dict:
                next_dict[each[1]] = [each[0]]
            else:
                next_dict[each[1]].append(each[0])

        for i in range(1, N+1):
            if i not in next_dict:
                next_dict[i] = []


        colors = [-1 for _ in range(N)]

        def isok(step, colors):
            # print(step, colors)
            for each in next_dict[step]:
                if colors[each-1] == -1:
                    pass
                if colors[each-1] == colors[step-1]:
                    return False
            return True

        def DFS(step):
            if step > N:
                return True

            for i in range(1, 5):
                colors[step-1] = i
                if isok(step, colors):
                    if DFS(step+1):
                        return True
                else:
                    colors[step - 1] = -1
            return False

        DFS(1)
        return colors




s = Solution()
print(s.gardenNoAdj(N = 4, paths =  [[1,2],[2,3],[3,1]]))

