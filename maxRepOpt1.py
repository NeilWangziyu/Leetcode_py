class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if len(text) == 0:
            return 0
        if len(text) == 1:
            return 1
        if len(text) == 2:
            if text[0] == text[1]:
                return 2
            else:
                return 1

        from collections import Counter
        res = 0
        counter = Counter(text)
        init = 1
        c = 1
        prev = text[0]
        while(init < len(text)):
            if text[init] == prev:
                c += 1
            elif init != len(text) - 1 and text[init+1]==prev:
            #     check further
                second_start = init + 2
                c_second = 1
                while (second_start < len(text)):
                    if text[second_start] == prev:
                        c_second += 1
                        second_start += 1
                    else:
                        break
                # print("c_second",c_second)
                # if c_second + c + 1> res:
                if counter[prev] >= c_second + c + 1:
                    res = max(res, c_second + c + 1)
                else:
                    res = max(res, c_second + c)

                prev = text[init]
                init = init + 1
                c = 1
                # print("prev", prev, "init", init)
                if init < len(text):
                    continue
                else:
                    return res

            else:
                # stop checking
                if counter[prev] >= c + 1:
                    res = max(res, c + 1)
                else:
                    res = max(res, c)
                prev = text[init]
                # print("prev", prev, init+1)
                c = 1
            init += 1

        # print("res", res, "c", c)
        return max(res, c)

s = Solution()
print(s.maxRepOpt1(text = "ababa"))
# 3
print(s.maxRepOpt1(text = "aaabaaa"))
# 6
print(s.maxRepOpt1(text = "aaabbaaa"))
# 4
print(s.maxRepOpt1(text = "aaaaa"))
# 5
print(s.maxRepOpt1(text = "abcdef"))
# 1
print(s.maxRepOpt1(text="baaabbabaabaabbaaababbbbaababbaabababa"))

print(s.maxRepOpt1(text="aabaaabaaaba"))
# 7
print(s.maxRepOpt1(text="aababbbbbbbbabababaabbbb"))
# 10
print("-----")
print(s.maxRepOpt1(text="bbababaaaa"))
# 6