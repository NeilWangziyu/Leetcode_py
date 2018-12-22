class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not "@" in S:
#             number
            raw_num = ""
            for each in S:
                if each.isdigit():
                    raw_num += each
            print(raw_num)
            if len(raw_num) == 10:
                return "***-***-" + raw_num[-4:]
            else:
                ragin = len(raw_num) - 10
                return "+"+ "*"*ragin +"-***-***-" + raw_num[-4:]
            # pass

        else:
#             EMAIL
            S = S.split('@')
            S[0] = S[0][0].lower() + "*****" +S[0][-1].lower() + "@"
            S[1] = S[1].lower()
            res = "".join(S)
            return res




S = "+(1213141241)-50-23431"

s = Solution()
print(s.maskPII(S))