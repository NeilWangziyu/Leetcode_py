class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # not a good method
        def is_sqrt(p):
            if p == 0 or p == 1:
                return True
            import math
            tem = int(math.sqrt(p))
            if tem ** 2 == p:
                return True
            else:
                return False

        if c == 0:
            return True
        if c == 1:
            return True
        if c == 2:
            return True
        i = 1
        while (i ** 2 <= c):
            p = c - i ** 2
            if is_sqrt(p):
                return True
            else:
                i += 1
        return False
    
    
    def judgeSquareSum2(self, c):
        L = 0
        R = int(c**0.5+1)
        while(R>=L):
            test = L**2+R**2
            if test == c:
                return True
            elif test < c:
                L += 1
            else:
                R -= 1

        return False
        

    def judgeSquareSum3(self,c):
        i = 2
        while(i**2<=c):
            count = 0
            if c % i == 0:
                while c%i == 0:
                    count += 1
                    c /= i
                if i%4 == 3 and count%2!=0:
                    return False
            i += 1
        return c%4 != 3





s = Solution()
print(s.judgeSquareSum3(100))