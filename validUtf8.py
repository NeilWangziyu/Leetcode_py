class Solution:
    def validUtf8(self, data) -> bool:
        if not data:
            return False

        i = 0
        while(i < len(data)):
            first_num = bin(data[i])[2:].zfill(8)
            if first_num[0] == '0':
                i += 1
            else:
                if first_num[:5] == '11110':
                    c = 3
                elif first_num[:4] == '1110':
                    c = 2
                elif first_num[:3] == '110':
                    c = 1
                else:
                    return False

                while(c > 0):
                    i += 1
                    c -= 1
                    if i >= len(data):
                        return False
                    that_num = bin(data[i])[2:].zfill(8)
                    # print(data[i], that_num)
                    if that_num[:2] != '10':
                        return False
                i += 1
        return True






s = Solution()
data = [197, 130, 1]
print(s.validUtf8(data))

data = [235, 140, 4]
print(s.validUtf8(data))

data =[237]

print(s.validUtf8(data))

data = [10]

print(s.validUtf8(data))

