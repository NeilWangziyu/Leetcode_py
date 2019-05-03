class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        rest = 0
        run = 0
        start = 0
        for i in range(len(gas)):
            run += (gas[i] - cost[i])
            rest += (gas[i] - cost[i])
            if (run < 0):
                start = i + 1
                run = 0
                print(start)
        if rest < 0:
            return -1
        else:
            return start


# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
s = Solution()
print(s.canCompleteCircuit(gas, cost))