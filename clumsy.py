class Solution:
    def clumsy(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1

        Num_list = list(range(N,0,-1))
        print(Num_list)
        string = ""
        list_of_operator = ["*", "//", "+", "-"]
        for i in range(N):
            string = string + str(Num_list[i])
            if i != N-1:
                string = string + list_of_operator[i%4]
        # print(string)
        return eval(string)

    def clumsy2(self, N: int) -> int:
        ans = [0, 1, 2, 6]
        if N == 1:
            return ans[1]
        elif N == 2:
            return ans[2]
        elif N == 3:
            return ans[3]
        res = N * (N - 1) // (N - 2) + (N - 3)
        # print(res)
        i = N - 4
        while i >= 4:
            res = res - i * (i - 1) // (i - 2) + (i - 3)
            # print(i, res)
            i -= 4
        res -= ans[i]
        return int(res)


s = Solution()
print(s.clumsy(10))