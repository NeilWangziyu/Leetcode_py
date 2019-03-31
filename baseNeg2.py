class Solution:
    def baseNeg2(self, N: int) -> str:
        """
        so hard
        补偿的思路
        :param N:
        :return:
        """
        if N == 0:
            return "0"
        t = N
        k = 1
        r = ""
        while(t!=0):
            if t % 2 == 1:
                r = '1' + r
                t -= k
            else:
                r = '0' + r
            t = t // 2
            k *= -1
        return r
N = 4
s = Solution()
print(s.baseNeg2(N))