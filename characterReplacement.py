import collections

class Solution:
    def characterReplacement(self, s, k: int) -> int:
        res, m, maxl = 0, collections.Counter(), 0
        for i in range(len(s)):
            m[s[i]] += 1
            maxl = max(maxl, m[s[i]])
            if res - maxl < k:
                res += 1
            else:
                m[s[i - res]] -= 1
        return res


    def characterReplacement2(self, s, k: int) -> int:
        n = len(s)
        res = 0
        count = [0] * 26
        le, maxc = 0, 0

        for ri in range(n):
            idx = ord(s[ri])-ord('A')
            count[idx] += 1

            if count[idx] > maxc:
                maxc = count[idx]

            if ri-le-maxc+1 > k:
                count[ord(s[le])-ord('A')] -= 1
                le += 1
            if ri-le+1>res:
                res = ri-le+1
        return res


str = "ABAB"
k = 2


s = Solution()
print(s.characterReplacement(str, k))

str = "ABAB"
k = 2

print(s.characterReplacement(str, k))

str = "AABABBA"
k = 1
print(s.characterReplacement(str, k))

str = "AAAB"
k = 0
print(s.characterReplacement(str, k))

str = "ABAA"
k = 0

print(s.characterReplacement(str, k))
