class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res = 0
        row = 0
        for each in S:
            # print(ord(each)-ord('a'))
            code = ord(each)-ord('a')
            res += widths[code]
            if res > 100:
                row += 1
                res = widths[code]
        if res == 0:
            return [row,res]
        else:
            return [row+1, res]



widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

S = "bbbcccdddaaa"
s = Solution()
print(s.numberOfLines(widths, S))
