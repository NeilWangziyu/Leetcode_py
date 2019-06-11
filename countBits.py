class Solution:
    def countBits(self, num: int):
        res = []
        for i in range(num+1):
            tem = list(bin(i)[2:])
            # print(tem.count('1'))
            res.append(tem.count('1'))
        return res

    def countBits2(self, num: int):
        ret = [0]
        n = 1
        while 2 ** n - 1 < num:
            ret += [1 + i for i in ret]
            n += 1
        ret += [1 + i for i in ret[:num - 2 ** (n - 1) + 1]]
        return ret


s = Solution()
print(s.countBits(5))