class Solution:
    def twoCitySchedCost(self, costs) -> int:
        if not costs:
            return 0

        length = len(costs)
        if length == 2:
            return min(costs[0][0] + costs[1][1], costs[0][1]+costs[1][0])

        sorted_Cost = sorted(costs, key=lambda x:x[0]-x[1])
        # print(sorted_Cost)
        res = 0
        for i in range(length//2):
            res += sorted_Cost[i][0]
        for i in range(length//2, length):
            res += sorted_Cost[i][1]
        return res








costs = [[10,20],[30,200],[400,50],[30,20]]
s = Solution()
print(s.twoCitySchedCost(costs=costs))