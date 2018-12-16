class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for each in A:
            tem = []
            for each_char in each[::-1]:
                if each_char == 1:
                    tem.append(0)
                else:
                    tem.append(1)
            res.append(tem)
        return res

    def flipAndInvertImage2(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for each in A:
            tem = []
            for each_char in each[::-1]:
                tem.append(1-each_char)
            res.append(tem)
        return res


S = Solution()
print(S.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))