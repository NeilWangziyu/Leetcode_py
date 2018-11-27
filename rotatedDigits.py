class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        good_list_char = ['6', '9', '2', '5']
        not_good_list_char = ['0', '1', '8']

        def is_good(num):
            flag = False
            for each in str(num):
                if each in good_list_char:
                    flag = True
                elif each not in not_good_list_char:
                    return False
            return flag


        count = 0
        for i in range(N + 1):
            if is_good(i):
                count += 1
        return count


s = Solution()
print(s.rotatedDigits(40))



