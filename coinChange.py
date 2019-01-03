class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(coins[0], len(dp)):
            for each in coins:
                if i - each >= 0:
                    dp[i] = min(dp[i], dp[i - each] + 1)


        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]


    def coinChange2(self, coins, amount):
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if i >= coins[j] and dp[i - coins[j]] != -1:
                    if dp[i] == -1 or dp[i] > dp[i - coins[j]] + 1:
                        dp[i] = dp[i - coins[j]] + 1
        return dp[amount]

#
# ---------------------
# 作者：Tianchi_M
# 来源：CSDN
# 原文：https: // blog.csdn.net / Tianchi_M / article / details / 82703935
# 版权声明：本文为博主原创文章，转载请附上博文链接！
#


coins = [2]

amount = 3

s = Solution()
print(s.coinChange(coins, amount))

print(s.coinChange2(coins, amount))

