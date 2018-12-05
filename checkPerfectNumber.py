class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num == 1:
        #     return False
        # res = 1
        #
        # for i in range(2, num//2+1):
        #     if num % i == 0:
        #         t = num // i
        #         if t > i:
        #             res += ic
        #             res += t
        #         elif t == i:
        #             res += i
        #
        # return res==num

        if num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336:
            return True
        else:
            return False







s = Solution()
print(s.checkPerfectNumber(100000000))

