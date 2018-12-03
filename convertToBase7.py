class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            flag = False
            num = abs(num)
        else:
            flag = True

        res_list = []
        while (num):
            left = num % 7
            num = num // 7
            res_list.append(str(left))
        res_list.reverse()
        res = "".join(res_list)
        if flag:
            return res
        else:
            return '-' + res


s = Solution()
print(s.convertToBase7(232))