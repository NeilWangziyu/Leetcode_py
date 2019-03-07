class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_f = 0
        a_b = 0
        b_f = 0
        b_b = 0
        if '+' in a:
            a_tem = a.split('+')
            a_f = int(a_tem[0])
            a_b = int(a_tem[1][:-1])
        else:
            a_f = int(a)

        if '+' in b:
            b_tem = b.split('+')
            b_f = int(b_tem[0])
            b_b = int(b_tem[1][:-1])
        else:
            b_f = int(a)

        res_1 = a_f * b_f
        res_2 = a_f * b_b
        res_3 = a_b * b_f
        res_4 = b_b * a_b * -1
        return str(res_1 + res_4) + '+' + str(res_2 + res_3) + 'i'

