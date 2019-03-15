class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        dp = [0 for _ in range(366)]
        isday = [False for _ in range(366)]
        for each in days:
            isday[each] = True

        for i in range(1, 366):
            if isday[i] == False:
                dp[i] = dp[i-1]
                continue

            dp[i] = dp[i-1] + costs[0]
            # 先默认买票

            if i >= 7:
                dp[i] = min(dp[i], dp[i-7]+costs[1])
            else:
                dp[i] = min(dp[i], costs[1])

            if (i >= 30):
                dp[i] = min(dp[i], dp[i - 30] + costs[2])
            else:
                dp[i] = min(dp[i], costs[2])
        print(dp)
        return dp[365]

    def mincostTickets2(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * 366
        days = set(days)
        for i in range(366):
            if i in days:

                dp[i] += dp[i - 1] + costs[0]

                if i > 7:
                    dp[i] = min(dp[i], dp[i - 7] + costs[1])
                else:
                    dp[i] = min(dp[i], costs[1])
                if i > 30:
                    dp[i] = min(dp[i], dp[i - 30] + costs[2])
                else:
                    dp[i] = min(dp[i], costs[2])
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,1,1]


s = Solution()
print(s.mincostTickets(days, costs))