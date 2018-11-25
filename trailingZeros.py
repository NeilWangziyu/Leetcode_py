class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<5:
            return 0
        tem = 5
        list = []
        while(tem<=n):
            x = n // tem
            list.append(x)
            tem *= 5

        return sum(list)





s = Solution()
print(s.trailingZeroes(400))
