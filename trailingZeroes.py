class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0

        while n >= 5:
            n = n // 5
            result += n

        return result


    def preimageSizeFZF(self, K: int) -> int:
        if K == 0:
            return 5
        if K == 1:
            return 5

        # after that, K at least 2

        low = 5
        high = 5000000000

        while(high > low + 1):
            mid = (high + low ) //2
            tem = self.trailingZeroes(mid)
            if tem == K:
                return 5
            elif K > tem:
                low = mid
            else:
                high = mid
        return 0

    # 10进制中只有2和5相乘才会得到10，也就是每有一对2和5，就多一个末尾的0
    #
    # 而阶乘又是从1开始乘到x，所以2的个数总是比5多，那么问题转化为求x！中有多少个5作为因子
    #
    # 公式为
    # k = x / 5 + x / 5 ^ 2 + x / 5 ^ 3 + ......



if __name__ == "__main__":
    s = Solution()
    # print(s.trailingZeroes(5000000000)//(10**9))
    print(s.preimageSizeFZF(121))