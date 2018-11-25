class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        pre_count = 0
        count = 9
        i = 1
        order = 9
        while (count < n):
            i += 1
            order *= 10
            pre_count = count
            count = count + i * order

        print(pre_count, count)
        print(i, order // 9)

        n = n - pre_count
        print(n)
        which_num = n // i
        which_digit = n % i
        if which_digit != 0:
            exact_num = order//9 - 1 + which_num + 1
            print(exact_num, which_digit)
            return str(exact_num)[which_digit-1]
        else:
            exact_num = order//9 - 1 + which_num
            print(exact_num, which_digit)
            return str(exact_num)[-1]


s = Solution()
print(s.findNthDigit(999999))