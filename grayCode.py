class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        # print bin(size)
        for i in range(2**n):
            print (i, bin(i), bin((i >> 1)), bin((i >> 1) ^ i) ) # 最后求异或
            res.append((i >> 1) ^ i)
        return res


s = Solution()
print(s.grayCode(3))