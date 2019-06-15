class Solution:
    # https: // blog.csdn.net / qq_17550379 / article / details / 85070792
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """

        dp = {0: 0}
        for x in rods:
            for d, y in list(dp.items()):
                dp[d + x] = max(dp.get(x + d, 0), y)
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
        return dp[0]



    def tallestBillboard2(self, rods) -> int:
        def function(s):
            result = {0: 0}
            for i in s:
                tmp = {}
                for j in list(result.keys()):
                    if j not in tmp:
                        tmp[j] = result[j]
                    else:
                        tmp[j] = max(tmp[j], result[j])

                    if i + j not in tmp:
                        tmp[i + j] = result[j]
                    else:
                        tmp[i + j] = max(result[j], tmp[i + j])

                    if abs(i - j) not in tmp:
                        tmp[abs(i - j)] = result[j] + min(i, j)
                    else:
                        tmp[abs(i - j)] = max(tmp[abs(i - j)], result[j] + min(i, j))

                result = tmp
            return result[0]

        return function(rods)



    def tallestBillboard3(self, rods):
        """
        DFS 思路
        :param rods:
        :return:
        放左边
        放右边
        不放
        """
        if len(rods) == 0 or len(rods) == 1:
            return 0

        self.res = 0

        rods.sort(reverse=True)
        remain = sum(rods)

        self.dfs(rods, remain - rods[0], 0, rods[0], 0)
        self.dfs(rods, remain - rods[0], 0, 0, 0)

        return self.res

    def dfs(self, rods, remain, i, left, right):
        if abs(left - right) > remain or (left + right +remain <= self.res * 2):
            return
        if left == right  and self.res < left:
            self.res = left

        i += 1
        if i == len(rods):
            return
        remain -= rods[i]
        self.dfs(rods, remain, i, left + rods[i], right)
        self.dfs(rods, remain, i, left, right + rods[i])
        self.dfs(rods, remain, i, left, right)





s = Solution()


print(s.tallestBillboard(rods=[1,2,3,4,5,6]))
print(s.tallestBillboard2(rods=[1,2,3,4,5,6]))
print(s.tallestBillboard3(rods=[1,2,3,4,5,6]))

print(s.tallestBillboard(rods=[1,2]))
print(s.tallestBillboard2(rods=[1,2]))
print(s.tallestBillboard3(rods=[1,2]))

print(s.tallestBillboard(rods=[1,2,3,6]))
print(s.tallestBillboard2(rods=[1,2,3,6]))
print(s.tallestBillboard3(rods=[1,2,3,6]))

