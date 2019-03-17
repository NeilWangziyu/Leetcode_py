class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 0
        n_str = str(bin(N))
        res = []
        for each in n_str[2:]:
            if each == '0':
                res.append('1')
            else:
                res.append('0')
        return int("".join(res),2)



s =Solution()
print(s.bitwiseComplement(10))
