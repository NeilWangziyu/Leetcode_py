class Solution:
    def isValid(self, S: str):
        if not S:
            return True

        if len(S) <= 2:
            return False

        while(True):
            stack = []
            if S == "abc":
                return True
            i = 0
            check = False
            while(i < len(S)):
                if i < len(S)-2:
                    if S[i:i+3] == 'abc':
                        i = i + 3
                        check = True
                    else:
                        stack.append(S[i])
                        i += 1
                else:
                    stack.append(S[i])
                    i += 1
            S = "".join(stack)
            if not S:
                return True
            if len(S) <= 2:
                return False
            if check == False:
                return False








S = "abcabc"

s = Solution()
print(s.isValid(S))