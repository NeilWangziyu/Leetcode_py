class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        利用 stack来做
        """
        s = bin(N)[2:]

        i = 0
        while(s[i] != '1'):
            i += 1
            if i == len(s):
                return 0

        max_c = 0
        count = 0
        for i in range(i, len(s)):
            if s[i] != '1':
                count += 1
            else:
                if count > max_c:
                    max_c = count
                count = 1

        return max_c




num = 8
s = Solution()
print(s.binaryGap(N=num))