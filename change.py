class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coin_list = [0 for _ in range(amount+1)]
        coin_list[0] = 1
        coins.sort()

        for j in range(len(coins)):
            for i in range(1, amount + 1):
                if i >= coins[j]:
                    coin_list[i] += coin_list[i - coins[j]]
        print(coin_list)
        return coin_list[-1]


    def change2(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(amount - c + 1):
                dp[i + c] = dp[i + c] + dp[i]
        return dp[amount]


amount = 5
coins = [1, 2, 5]

s = Solution()
print(s.change(amount, coins))
