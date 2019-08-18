class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 和下一个排列一样
        if n <= 11:
            return -1

        n_list = list(map(int, list(str(n))))
        if n_list == sorted(n_list, reverse=True):
            return -1
        n_max_min = []
        for i in range(len(n_list)-1, -1, -1):
            if not n_max_min:
                n_max_min.append(n_list[i])
            else:
                if n_list[i] < max(n_max_min):
                    if len(n_max_min) > 1:
                        n_max_min.sort()
                        for j in range(len(n_max_min)):
                            if n_max_min[j] > n_list[i]:
                                replace = n_max_min[j]
                                n_max_min.pop(n_max_min.index(replace))
                                res_list = n_list[:i] + [replace] + sorted(n_max_min + [n_list[i]])
                                if int("".join(map(str, res_list))) <= 2 ** 31 - 1:
                                    return int("".join(map(str, res_list)))
                                else:
                                    return -1
                    else:
                        res_list = n_list[:i] + n_max_min + [n_list[i]]
                        if int("".join(map(str, res_list))) <= 2**31 - 1:
                            return int("".join(map(str, res_list)))
                        else:
                            return -1
                else:
                    n_max_min.append(n_list[i])

        return -1




s = Solution()
n = 12
print(s.nextGreaterElement(n))

n = 21
print(s.nextGreaterElement(n))

n = 9001233129
print(s.nextGreaterElement(n))

n =230241
print(s.nextGreaterElement(n))

n =2147483647
print(s.nextGreaterElement(n))

n =1999999999
print(s.nextGreaterElement(n))