class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividingNumber(i):
            list_divide = list(str(i))
            for each in list_divide:
                if each == "0":
                    return False
                else:
                    if i % int(each) != 0:
                        return False
            return True


        res = []
        for i in range(left, right+1):
            if isSelfDividingNumber(i):
                res.append(i)
        return res


s = Solution()
print(s.selfDividingNumbers(1, 22))
