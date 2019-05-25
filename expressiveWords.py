class Solution:
    def expressiveWords(self, S: str, words) -> int:
        if not S:
            return 0
        S_list = []
        init_num = 0
        init_char = S[0]
        for i in range(len(S)):
            if S[i] == init_char:
                init_num += 1
            else:
                S_list.append((init_char, init_num))
                init_char = S[i]
                init_num = 1
        if init_num != 0:
            S_list.append((init_char, init_num))
        # print(S_list)


        res = 0
        for each in words:
            tem_list = []

            init_num = 0
            init_char = each[0]
            for i in range(len(each)):
                if each[i] == init_char:
                    init_num += 1
                else:
                    tem_list.append((init_char, init_num))
                    init_char = each[i]
                    init_num = 1
            if init_num != 0:
                tem_list.append((init_char, init_num))
            # print(tem_list)
            found = True
            if len(S_list) != len(tem_list):
                found = False
                continue
            for i in range(len(S_list)):
                if S_list[i][0] != tem_list[i][0]:
                    found = False
                    break
                if S_list[i][1] < tem_list[i][1]:
                    found = False
                    break
                if S_list[i][1] > tem_list[i][1] and S_list[i][1]<3:
                    found = False
                    break
            if found:
                res += 1
        return res





# S = "heeellooo"
# words = ["hello", "hi", "helo"]


S ="aaa"
words = ["aaaa"]
s = Solution()
print(s.expressiveWords(S, words))

S ="abcd"
words = ["abc"]
print(s.expressiveWords(S, words))

S = "heeellooo"
words = ["hello", "hi", "helo"]
print(s.expressiveWords(S, words))
