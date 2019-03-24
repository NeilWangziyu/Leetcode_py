class Solution:
    def ambiguousCoordinates(self, S: str):
        def check_str(str):
            if not str:
                return []
            if len(str) == 1:
                return [str]
            if str[0] == '0':
                if str[-1] == '0':
                    return []
                else:
                    return [[str[0]]+['.']+str[1:]]
            else:
                if str[-1] == '0':
                    return [str]
                else:
                    res = []
                    for i in range(1,len(str)):
                        res.append(str[:i]+['.']+str[i:])
                    res.append(str)
                    return res


        if S == "()":
            return []

        str_num = list(S[1:-1])
        if len(str_num) == 1:
            return []
        # print(str_num)
        reslist = []
        for i in range(1,len(str_num)):
            first_part = str_num[:i]
            second_part = str_num[i:]
            first_part_str = check_str(first_part)
            second_part_str = check_str(second_part)

            if first_part_str and second_part_str:
                for each_str1 in first_part_str:
                    for each_str2 in second_part_str:
                        reslist.append("("+"".join(each_str1)+", "+"".join(each_str2)+")")
        return reslist











s = Solution()
print(s.ambiguousCoordinates("(00011)"))

print(s.ambiguousCoordinates("(123)"))
print(s.ambiguousCoordinates("(0123)"))