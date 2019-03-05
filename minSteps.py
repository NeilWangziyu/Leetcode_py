class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 0
        if n == 2:
            return 2

        dp_list = [n for n in range(n+1)]
        dp_list[1] = 0
        # print(dp_list)
        for i in range(3, n+1):
            j = 1
            list = []
            while(j<=i//2):
                if i % j == 0:
                    list.append(j)
                j += 1

            # print(i, list)
            check_list = []
            for each in list:
                check_list.append(dp_list[each]+i//each)
            # print(check_list)
            dp_list[i] = min(check_list)

        return dp_list[n]

    def minSteps2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        for i in range(n - 1, 1, -1):
            if n % i == 0:
                return self.minSteps(i) + (n // i)
        return n


    def minSteps3(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n + 1):
            while n % i == 0:
                res += i
                n = n // i
        return res


s = Solution()
print(s.minSteps2(30))
print(s.minSteps3(30))
