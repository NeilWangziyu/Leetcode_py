class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        #
        # dp = [i for i in range(n+1)]
        # for i in range(n+1):
        #     k = 2
        #     while(k**2 <= i):
        #         dp[i] = min(dp[i], dp[i-k**2]+1)
        #         k += 1
        #
        # print(dp)
        # return dp[n]


        while n % 4 == 0:
            n /= 4

        if n % 8 == 7:
            return 4

        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)

            a += 1
        return 3


s = Solution()
print(s.numSquares(1558))