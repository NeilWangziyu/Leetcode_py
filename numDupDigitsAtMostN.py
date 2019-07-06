class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        """
        超时
        :param N:
        :return:
        """
        if N <= 10:
            return 0
        res = 0
        for i in range(10, N+1):
            len_it_self = len(str(i))
            len_set = len(set(str(i)))
            if len_set < len_it_self:
                res += 1
        return res

    def numDupDigitsAtMostN2(self, N: int) -> int:
        """
        math problem
        :param N:
        :return:
        """
        def count(mask, num):
            if num > N:
                return 0
            ret = 1
            if num == 0:
                nd = 1
            else:
                nd = 0
            while(nd < 10):
                if (mask>>nd) & 1 == 0:
                    ret += count(mask | (1 << nd), num * 10 + nd)
                nd += 1
            return ret

        return N + 1 - count(0, 0)





s = Solution()
# print(s.numDupDigitsAtMostN(10000))
print(s.numDupDigitsAtMostN2(100000000))