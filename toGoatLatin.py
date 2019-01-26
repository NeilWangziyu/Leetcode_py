class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        start = set(["a","e","i","o","u","A","E", "I", "O", "U"])

        S = S.split(" ")
        res = []
        for index, each in enumerate(S):
            if each[0] in start:
                res.append(each + "ma"+"a"*(index+1))
            else:
                if len(each) == 1:
                    res.append(each + "ma"+"a"*(index+1))
                else:

                    res.append(each[1:]+each[0] +"ma"+"a"*(index+1))

        return " ".join(res)


S = "Each word consists of lowercase and uppercase letters only"

s = Solution()
print(s.toGoatLatin(S))