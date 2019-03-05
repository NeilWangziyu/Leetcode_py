class Solution:
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                profit += prices[i] - prices[i - 1]
        return profit

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
        return profit

    def maxProfit3(self, prices):
        """
        sell[i]表示截至第i天，最后一个操作是卖时的最大收益；
        buy[i]表示截至第i天，最后一个操作是买时的最大收益；
        cool[i]表示截至第i天，最后一个操作是冷冻期时的最大收益；
        递推公式：
        sell[i] = max(buy[i-1]+prices[i], sell[i-1]) (第一项表示第i天卖出，第二项表示第i天冷冻)
        buy[i] = max(cool[i-1]-prices[i], buy[i-1]) （第一项表示第i天买进，第二项表示第i天冷冻）
        cool[i] = max(sell[i-1], buy[i-1], cool[i-1])
        """
        if not price:
            return 0

        sell = [0 for _ in range(len(price))]
        buy  = [0 for _ in range(len(price))]
        cool = [0 for _ in range(len(price))]
        buy[0] = -prices[0]
        for i in range(1, len(price)):
            sell[i] = max(buy[i-1]+price[i], sell[i-1])
            buy[i] = max(cool[i-1] - price[i], buy[i-1])
            cool[i] = max(sell[i-1], buy[i-1], cool[i-1])

        print(sell)
        print(buy)
        print(cool)
        return max(sell[-1], buy[-1], cool[-1])

    def maxProfit3_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        buy = [0 for _ in range(0, n)]
        sell = [0 for _ in range(0, n)]
        buy[0] = -prices[0]
        sell[0] = 0
        for i in range(1, n):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            if i < 2:
                buy[i] = max(buy[i - 1], -prices[i])
            else:
                buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])

        print(sell)
        print(buy)
        return sell[n - 1]


if __name__ == "__main__":
    price = [1,2,3,0,2]
    s = Solution()
    print(s.maxProfit3(price))
    print(s.maxProfit3_1(price))