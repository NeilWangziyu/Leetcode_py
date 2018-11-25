class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            if int(s) <= 26:
                if s != '10' and s != '20':
                    return 2
                else:
                    return 1
            else:
                if s[1] == 0:
                    return 0
                else:
                    return 1

        res = []
        for i in range(len(s)):
            res.append(0)

        if s[-1]==0:
            res[-1] = 0
        else:
            res[-1] = 1



        for i in range(-1, -len(s)):
            pass




        if int(s[:2]) > 26:
            return self.numDecodings(s[1:])
        else:
            if s[:2] == '10' or s[:2] == '20':
                return self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])




s = Solution()
print(s.numDecodings("501"))