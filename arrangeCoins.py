class Solution:
    def arrangeCoins(self, k):
        """
        :type n: int
        :rtype: int
        """
        n = 0
        while((1+n)*n/2 <= k):
            n += 1
        if (1+n)*n/2 == k:
            return n
        else:
            return n-1


    def arrangeCoin2(self, n):
        """
        :type n: int
        :rtype: int
        天才啊二分法
        """
        if n <= 1:
            return n
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) / 2 <= n:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1



s = Solution()
print(s.arrangeCoins(10))