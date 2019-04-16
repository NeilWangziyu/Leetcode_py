class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        res = ""
        for each in S:
            if each.isalpha():
                res += each
            elif each.isdigit():
                res = res * int(each)

            if len(res) >= K:
                print(res)
                return res[K-1]


    def decodeAtIndex2(self, S: str, K: int) -> str:
        length = 0
        for each in S:
            if each.isalpha():
                length += 1
            else:
                length *= int(each)
        S = S[::-1]
        for each in S:
            # 一般来说，当解码的字符串等于某个长度为
            # size
            # 的单词重复某些次数（例如
            # apple
            # 与
            # size = 5
            # 组合重复6次）时，索引
            # K
            # 的答案与索引
            # K % size
            # 的答案相同。


            K = K % length
            if K == 0 and each.isalpha():
                return each

            if each.isdigit():
                length = length // int(each)
            else:
                length -= 1

    def decodeAtIndex3(self, S, K):
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1




    # 可以想办法在原始S中求第K，1.
    # 算出展开S的长度为N，2
    # 所求位置为k % S。因此倒序遍历S，遇见数字N = N / d，遇见字幕N = N - 1;
    # 直到K % N == 0。输出此处字符



if __name__ == "__main__":
    S = "leet2code3"
    K = 10
    s = Solution()
    print(s.decodeAtIndex(S, K))
    print(s.decodeAtIndex2(S, K))

    S = "ha22"
    K = 5
    print(s.decodeAtIndex(S, K))
    print(s.decodeAtIndex2(S, K))

    S = "a2345678999999999999999"
    K = 1
    print(s.decodeAtIndex(S, K))
    print(s.decodeAtIndex2(S, K))
    S = "a23"
    K = 6
    print(s.decodeAtIndex(S, K))
    print(s.decodeAtIndex2(S, K))

    S = "y75lgfqyn4re8treuyrs9pqxfgvf3rrtqxr6lrm8ymxawwf97jcm5itz8dpvjig3o9iartdajjeoo58ipu6wmuozzpjzzfzrciy6"
    K = 292404628
    # print(s.decodeAtIndex(S, K))
    print(s.decodeAtIndex2(S, K))

    S = "ixm5xmgo78"
    K = 711
    print(s.decodeAtIndex(S, K))
    print(s.decodeAtIndex2(S, K))