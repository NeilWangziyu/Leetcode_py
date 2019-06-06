class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return ""
        res = ""
        for i in range(1, len(str2)+1):
            tem = str2[:i]
            # print(tem)
            factor1 = int(len(str1) / len(tem))
            factor2 = int(len(str2) / len(tem))
            if tem * factor1 == str1 and tem * factor2 == str2:
                res = tem
        return res





s = Solution()
print(s.gcdOfStrings("LEET","ABAB"))
