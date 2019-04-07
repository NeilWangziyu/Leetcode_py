class Solution:
    def integerReplacement(self, n: int) -> int:
        # 用位运算，最后一位是0直接右移，最后两位都是1，且该数不是3是，就选择+1，否则就选择－1，直到该数变成1，为防止越界
        count = 0
        while (n != 1):
            if n % 2 == 0:
                n = n >> 1
            else:
                if bin(n)[-2:] == '11' and n != 3:
                    n = n + 1
                else:
                    n = n - 1
            count += 1

        return count

s = Solution()
print(s.integerReplacement(45))