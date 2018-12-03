class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))

        # if len(a)!=len(b):
        #     return max(len(a), len(b))



s = Solution()
print(s.findLUSlength("ee",'ee'))