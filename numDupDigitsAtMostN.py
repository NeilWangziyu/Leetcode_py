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
        if N <= 10:
            return 0





s = Solution()
print(s.numDupDigitsAtMostN(101))