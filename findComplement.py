class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)[2:]
        res = ""
        for each in num:
            if each == '1':
                res += '0'
            else:
                res += '1'
        return int(res, 2)


s = Solution()
print(s.findComplement(34))
