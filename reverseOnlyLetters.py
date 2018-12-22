class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        num = []
        else_num = []
        else_index = []
        S = list(S)
        print(S)
        for index, char in enumerate(S):
            if char.isalpha():
                num.append(char)
            else:
                else_num.append(char)
                else_index.append(index)
        # print(else_num, num, else_index)
        num = num[::-1]
        S = S[::]
        for i in range(len(S)):
            if else_index:
                if i == else_index[0]:
                    S[i] = else_num[0]
                    else_index.pop(0)
                    else_num.pop(0)
                else:
                    S[i] = num.pop(0)
            else:
                S[i] = num.pop(0)
        return "".join(S)



s = Solution()
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))