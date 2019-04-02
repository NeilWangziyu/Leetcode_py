class Solution:
    def baseNeg2(self, N: int) -> str:
        """
        so hard
        补偿的思路
        :param N:
        :return:
        """
        if N == 0:
            return "0"
        t = N
        k = 1
        r = ""
        while(t!=0):
            if t % 2 == 1:
                r = '1' + r
                t -= k
            else:
                r = '0' + r
            t = t // 2
            k *= -1
        return r

    def baseNeg2_2(self, N: int) -> str:
        """
        空虚解法
        :param N:
        :return:
        """
        if N == 0:
            return '0'
        list_tail = ['0b000', '0b001', '0b110', '0b111', '0b1001']
        list_start = [0, 0, 1, 1]
        res_string = ''
        trigger = '0b0'
        while N != 0:
            num = N % 4
            tmp_string = list_tail[num]
            trigger = int(tmp_string[:3], 2)
            res_string = tmp_string[-2:] + res_string
            N = N // 4 + trigger

        res_string = res_string.lstrip('0')
        return res_string

N = 4
s = Solution()
print(s.baseNeg2(N))