class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 3:
            return True
        print(bin(n))
        bin_n = bin(n)[2:]
        first = len(bin_n) - 1
        while(first>=1):
            if bool(int(bin_n[first])) == bool(int(bin_n[first-1])):
                return False
            first -= 1
        return True

n = 3
s = Solution()
print(s.hasAlternatingBits(n))