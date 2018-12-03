class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        start = 0
        length = len(s)
        s = list(s)
        while (length > start + 2*k):
            s[start:start + k] = s[start:start + k][::-1]
            start = start + 2*k

        if (length - start <= 2*k) and (length - start >= k):
            s[start:start + k] = s[start:start + k][::-1]
        else:
            s[start::] = s[start:][::-1]

        return "".join(s)

s = Solution()
print(s.reverseStr(s = "abcdefg", k = 8))


