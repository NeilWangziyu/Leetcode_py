from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if not tokens:
            return 0
        tokens.sort()
        if tokens[0] > P:
            return 0
        max_res = 0
        res = 0
        while(tokens):
            if tokens[0] <= P:
                P -= tokens[0]
                tokens.pop(0)
                res += 1
                max_res = max(max_res, res)
            else:
                if res == 0:
                    break
                else:
                    res -= 1
                    P += tokens[-1]
                    tokens.pop(-1)
        return max_res

    def bagOfTokensScore2(self, tokens: List[int], P: int) -> int:
        res = 0
        L = [0]
        tokens.sort()
        i, j = 0, len(tokens) - 1
        while i <= j:
            if tokens[i] < P:
                P = P - tokens[i]
                res += 1
                i += 1
                L.append(res)
            else:
                if tokens[i] == P:
                    L.append(res + 1)
                if res == 0:
                    break
                P = P + tokens[j]
                res -= 1
                j -= 1
        return max(L)

s = Solution()

tokens = [100, 200]
P = 150
print(s.bagOfTokensScore(tokens, P))

tokens = [100,200]
P = 150
print(s.bagOfTokensScore(tokens, P))

tokens = [100,200,300,400]
P = 200
print(s.bagOfTokensScore(tokens, P))

