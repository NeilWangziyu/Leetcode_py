class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # init_1 = len(num1)-1
        # init_2 = len(num2)-1
        # c = 0
        # res = ""
        # while(init_1>=0 and init_2 >= 0):
        #     print(num1[init_1], num2[init_2])
        #     tem = ord(num1[init_1]) + ord(num2[init_2])-ord('0') + c
        #     if tem > ord('9'):
        #         tem = tem - ord('9') - 1
        #         print(chr(tem))
        #         c = 1
        #     else:
        #         c = 0
        #     print(chr(tem))
        #     res = chr(tem) + res
        #
        #     init_1 -= 1
        #     init_2 -= 1
        #     print(res)
        # if init_1 < 0 and init_2 < 0:
        #     return res
        # elif init_1 < 0 and init_2 > 0:
        #     print(res,c)
        #     if c == 0:
        #         return num2[:init_2+1]+res
        #     else:
        #         while(init_2 >=0):
        #             tem = ord(num2[init_2]) + c
        #             if tem > ord('9'):
        #                 tem = tem - ord('9')
        #                 c = 1
        #             else:
        #                 c = 0
        #             res = chr(tem) + res
        #             init_2 -= 2
        # else:
        #     print(res,c)
        #     if c == 0:
        #         return num1[:init_1+1] + res
        #     else:
        #         while (init_1>=0):
        #             tem = ord(num1[init_1])+ c
        #             if tem > ord('9'):
        #                 tem = tem - ord('9')
        #                 c = 1
        #             else:
        #                 c = 0
        #             res = chr(tem) + res
        #             init_1 -= 1
        # if c == 0:
        #     return res
        # else:
        #     return '1'+res
        return int(num1) + int(num2)





num1 = "1119"
num2 = "4"
s = Solution()
print(s.addStrings(num1, num2))