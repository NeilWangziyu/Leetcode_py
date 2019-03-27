class Solution:
    def maximumSwap(self, num: int) -> int:
        if not num:
            return num
        if num < 10:
            return num
        init = 0
        # num_list = list(map(int, list(str(num))))
        num_list = list(str(num))
        while(init < len(num_list)):
            met_max_first = num_list[init]
            met_max_first_index = init
            for i in range(init, len(num_list)):
                if num_list[i] >= met_max_first:
                    met_max_first = num_list[i]
                    met_max_first_index = i

            if met_max_first == num_list[init]:
                init += 1
                continue
            else:
                num_list[init], num_list[met_max_first_index] = num_list[met_max_first_index], num_list[init]
                break

        return int("".join(num_list))

    def maximumSwap2(self, num):
        num1 = list(str(num))
        # print(num1)
        for i in range(0, len(num1) - 1):
            if num1[i] < max(num1[i + 1:]):
                max_int = max(num1[i + 1:])
                for j in range(len(num1) - 1, i, -1):
                    if num1[j] == max_int:
                        num1[i], num1[j] = num1[j], num1[i]
                        # print(num1[i],index_int,max_int)
                        return int("".join(num1))

        return num


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSwap(1993))