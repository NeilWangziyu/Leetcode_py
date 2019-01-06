class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict_alphabet = {}
        for index, each in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            dict_alphabet[each] = index + 1
        res = 0
        count = 0
        for each in s[::-1]:

            res += dict_alphabet[each] * 26**count
            count += 1
        return res

t = "AB"
s = Solution()
print(s.titleToNumber(t))