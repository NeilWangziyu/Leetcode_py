class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        list_tail = ['0b000', '0b001', '0b110', '0b111', '0b1001']
        # list_start = [0, 0, 1, 1]
        res_string = ''
        # trigger = '0b0'
        while N != 0:
            num = N % 4
            tmp_string = list_tail[num]
            trigger = int(tmp_string[:3], 2)
            res_string = tmp_string[-2:] + res_string
            N = N // 4 + trigger

        res_string = res_string.lstrip('0')
        return res_string

    def addNegabinary(self, arr1, arr2):
        arr1_num = 0
        arr1 = arr1[::-1]
        for i in range(len(arr1)):
            if arr1[i] == 1:
                arr1_num += (-2) ** (i)
        # print(arr1_num)

        arr2_num = 0
        arr2 = arr2[::-1]
        for i in range(len(arr2)):
            if arr2[i] == 1:
                arr2_num += (-2) ** (i)
        # print(arr2_num)

        sum_num = arr1_num + arr2_num
        sum_num_str = self.baseNeg2(sum_num)
        res = list(map(int, list(sum_num_str)))
        return res


s = Solution()
arr1 = [1,1,1,1,1]
arr2 = [1,0,1]
print(s.addNegabinary(arr1, arr2))