class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <2:
            return 0
        odd_list = [True] * n
        odd_list[0] = False
        odd_list[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if odd_list[i]:
                j = 2
                while(i*j<n):
                    odd_list[i*j] = False
                    j += 1
        # print(odd_list)
        ans = odd_list.count(True)
        return ans


s = Solution()
print(s.countPrimes(50))