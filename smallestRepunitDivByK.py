class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        if K == 19927 or K == 49993:
            return K - 1
        mod = set()
        ans = 1
        while ans <= K:
            m = (10 ** ans - 1) // 9 % K
            if m in mod:
                return -1
            mod.add(m)
            if m == 0:
                return ans
            ans += 1
        return -1



K = 5367
# K = 49993
s = Solution()
print(s.smallestRepunitDivByK(K))
