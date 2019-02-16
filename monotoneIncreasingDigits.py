class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        N_str = list(str(N))
        if len(N_str) == 1:
            return
        length = len(N_str)
        init = N_str[-1]
        for i in range(length-1, -1, -1):
            if N_str[i] > init:
                for j in range(i+1, length):
                    N_str[j] = '9'
                N_str[i] = str(int(N_str[i])-1)
                init = N_str[i]
            else:
                init = N_str[i]
        print(N_str)
        return int("".join(N_str))





N = 100
s = Solution()
print(s.monotoneIncreasingDigits(N))