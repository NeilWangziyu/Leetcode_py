class Solution:
    def toHex(self, num: int) -> str:
        hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                    12: 'c',
                    13: 'd', 14: 'e', 15: 'f'}

        if num == 0:
            return '0'
        if num < 0:
            num += 2**32
        res = ""
        while(num > 0):
            res += hex_dict[num % 16]
            num = num // 16
        # print(res[::-1])

        return res[::-1]

#     modify string is more consuming than modify list



s = Solution()
print(s.toHex(-1))