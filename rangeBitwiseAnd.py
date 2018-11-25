class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = bin(m)[2:]
        n = bin(n)[2:]
        m = "0" * (31-len(m)) + m
        n = "0" * (31-len(n)) + n

        arr = ["0" for _ in range(31)]
        for i in range(31):
            if m[i] != n[i]:
                break
            else:
                if m[i] == '1' and n[i] == '1':
                    arr[i] = '1'

        # print(arr)
        str = "".join(arr)
        return int(str, 2)



s = Solution()
print(s.rangeBitwiseAnd(5, 7))
