class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0

        res = 0
        start = s[0]
        this_num = 1

        prev_num = 0
        for i in range(1,len(s)):
            if s[i] == start:
                this_num += 1
                if prev_num > 0:
                    prev_num -= 1
                    res += 1
                    print(i)

            else:
                prev_num = this_num
                this_num = 1
                start = s[i]
                if prev_num > 0:
                    prev_num -= 1
                    res += 1
                    # print(i)
        return res


s = Solution()
print(s.countBinarySubstrings("10101"))