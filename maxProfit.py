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

    def maxProfit_freeze(self, prices):
        """
        309. 最佳买卖股票时机含冷冻期
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

    def maxProfit_freeze_1(self, prices):
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


    def maxProfit_With_fee(self, prices, fee: int) -> int:
        if not prices:
            return 0
        # have share
        hold = [0 for _ in range(len(prices))]

        sell = [0 for _ in range(len(prices))]
        hold[0] = - prices[0]
        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i-1], hold[i-1] - fee + prices[i])
        return sell[-1]


    def maxProfit_3(self, prices) -> int:
        if not prices:
            return 0
        hold1 = [0 for _ in range(len(prices))]
        sell1 = [0 for _ in range(len(prices))]
        hold2 = [0 for _ in range(len(prices))]
        sell2 = [0 for _ in range(len(prices))]

        hold1[0] = - prices[0]
        hold2[0] = - prices[0]
        for i in range(1, len(prices)):
            hold1[i] = max(hold1[i-1], - prices[i])
            sell1[i] = max(sell1[i-1], hold1[i-1] + prices[i])
            hold2[i] = max(hold2[i-1] , sell1[i-1] - prices[i])
            sell2[i] = max(sell2[i-1], hold2[i-1] + prices[i])
        return sell2[-1]


    def maxProfit_3_1(self, prices) -> int:
        """
        更小的空间复杂度
        :param prices:
        :return:
        """
        if not prices:
            return 0
        hold1 = - prices[0]
        sell1 = 0
        hold2 = - prices[0]
        sell2 = 0

        for i in range(1, len(prices)):
            hold1 = max(hold1, - prices[i])
            sell1 = max(sell1, hold1 + prices[i])
            hold2 = max(hold2 , sell1 - prices[i])
            sell2 = max(sell2, hold2 + prices[i])

        return sell2



    def maxProfit_4(self, k: 'int', prices):
        if not prices:
            return 0
        if k == 0:
            return 0
        if k < len(prices):
            hold = [-prices[0] for _ in range(k)]
            sell = [0 for _ in range(k)]

            for i in range(1, len(prices)):
                for index in range(k):
                    if index == 0:
                        hold[index] = max(hold[index], -prices[i])
                        sell[index] = max(sell[index], hold[index] + prices[i])
                    else:
                        hold[index] = max(hold[index], sell[index - 1] - prices[i])
                        sell[index] = max(sell[index], hold[index] + prices[i])
            return sell[-1]
        else:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] - prices[i-1] > 0:
                    profit += prices[i] - prices[i-1]
            return profit












if __name__ == "__main__":
    price = [1,2,3,0,2]
    s = Solution()
    print(s.maxProfit_freeze(price))
    print(s.maxProfit_freeze_1(price))
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(s.maxProfit_With_fee(prices, fee))

    prices = [3,3,5,0,0,3,1,4]
    print(s.maxProfit_3(prices))

    prices =[7,6,4,3,1]
    print(s.maxProfit_3(prices))
    print(s.maxProfit_3_1(prices))
    print("______________________")


    prices=[3,3,5,0,0,3,1,4]
    print(s.maxProfit_3_1(prices))

    k = 2
    print(s.maxProfit_4(k, prices))