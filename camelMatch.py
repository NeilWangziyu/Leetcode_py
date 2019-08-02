from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        if not queries:
            return []

        pattern_list = list(pattern)
        res = []
        for each in queries:
            i = 0
            j = 0
            while(i < len(each)):
                if j >= len(pattern) and each[i].islower():
                    i += 1
                elif j >= len(pattern) and each[i].isupper():
                    break
                else:
                    if each[i] == pattern[j]:
                        i += 1
                        j += 1
                    elif each[i].islower():
                        i +=1
                    elif each[i].isupper():
                        break
            if i >= len(each) and j >= len(pattern):
                res.append(True)
            else:
                res.append(False)
        return res





queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FB"

s = Solution()
print(s.camelMatch(queries, pattern))

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBa"

s = Solution()
print(s.camelMatch(queries, pattern))

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"


s = Solution()
print(s.camelMatch(queries, pattern))
