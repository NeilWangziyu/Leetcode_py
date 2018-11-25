class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dict_excel = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
                      13: 'M', 14: 'N',
                      15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
                      26: 'Z'}
        return_list = []
        while (n > 26):
            if n % 26 == 0:
                letter = (n - 1) % 26 + 1
                next_n = (n - 1) // 26
            else:
                letter = n % 26
                next_n = n // 26
            return_list.append(dict_excel[letter])
            n = next_n

        return_list.append(dict_excel[n])
        return_list.reverse()
        res = ''.join(return_list)
        return res


s = Solution()
print(s.convertToTitle(703))
