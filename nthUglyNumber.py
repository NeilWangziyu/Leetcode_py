class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # attention this dynamic programming method

        ugly = [0 for _ in range(n)]
        ugly[0] = 1
        index = [0 for _ in range(3)]
        for i in range(1, n):
            a = ugly[index[0]] * 2
            b = ugly[index[1]] * 3
            c = ugly[index[2]] * 5
            next = min(a, min(b, c))
            if next == a:
                index[0] += 1
            if next == b:
                index[1] += 1
            if next == c:
                index[2] += 1
            ugly[i] = next

        return ugly[-1]

        # max_len = 2123366400
        #
        # list_ugly = [False] * (max_len+1)
        # list_ugly[1] = True
        #
        # for i in range(max_len+1):
        #     if list_ugly[i]:
        #         if i*3<=max_len:
        #             list_ugly[i*3] = True
        #         if i*2<=max_len:
        #             list_ugly[i*2] = True
        #         if i*5<=max_len:
        #             list_ugly[i*5] = True
        #
        # count = 0
        # print(list_ugly[:20])
        # for i in range(max_len+1):
        #     if list_ugly[i]:
        #         count += 1
        #     if count == n:
        #         return i


s = Solution()
print(s.nthUglyNumber(20))
