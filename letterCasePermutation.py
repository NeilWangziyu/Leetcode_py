class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def DFS(index, str):
            if index >= len(str):
                return
            if str[index].isalpha():
                if str[index].islower():
                    s_check = str[index].upper()
                    if index == len(str) - 1:
                        res.append(str[:index]+s_check)
                        DFS(index + 1, str[:index] + s_check)
                        DFS(index + 1, str)
                    else:
                        res.append(str[:index] + s_check + str[index+1:])
                        DFS(index+1, str[:index] + s_check + str[index+1:])
                        DFS(index + 1, str)
                else:
                    s_check = str[index].lower()
                    if index == len(str) - 1:
                        res.append(str[:index] + s_check)
                        DFS(index + 1, str[:index] + s_check)
                        DFS(index + 1, str)
                    else:
                        res.append(str[:index] + s_check + str[index + 1:])
                        DFS(index + 1, str[:index] + s_check + str[index + 1:])
                        DFS(index + 1, str)
            else:
                DFS(index + 1, str)



        res = [S]
        if not S:
            return res
        DFS(0, S)
        return res
        # for i in range(len(S)):
        #     print(S[i])
        #     print(S[i].isalpha())
        #     if S[i].isalpha():


str = "C"
S = Solution()
print(S.letterCasePermutation(str))