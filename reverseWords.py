class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        # s.reverse()
        print(s)
        return " ".join(s[::-1])




s = Solution()
print(s.reverseWords("the sky is blue"))