class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def is_prime(num):
            if num <2 or num == 4:
                return False
            if num in [2,3,5,7]:
                return True
            i = 2
            while(i**2<=num):
                if num % i == 0:
                    return False
                else:
                    i += 1
            return True


        res = 0
        for i in range(L, R+1):
            bin_num = bin(i)[2:]
            count = 0
            for each in bin_num:
                if each == '1':
                    count += 1
            # print(bin_num,count)
            if is_prime(count):
                res += 1
                print(count)

        return res

    def countPrimeSetBits2(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for i in range(L, R+1):
            if bin(i).count('1') in prime:
                count += 1
        return count




s = Solution()
print(s.countPrimeSetBits(L = 990, R = 1048))