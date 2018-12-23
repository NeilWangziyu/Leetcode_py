class Solution:
    # 物理题，很有意思
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        m, n = q, p
        while m & 1 == 0 and n & 1 == 0:
            m, n = m / 2, n / 2
#         变成最小的偶数
        if m & 1 == 0 and n & 1 == 1:
            return 0
#         q是偶数，p是奇数
        elif m & 1 == 1 and n & 1 == 1:
            return 1
        elif m & 1 == 1 and n & 1 == 0:
            return 2







# p = 2
# q = 1

p = 3
q = 1
# 1
s = Solution()
print(s.mirrorReflection(p,q))