class Solution:
    def longestDupSubstring(self, S):
        # 后缀数组
        # 如果某个子串在目标字符串中出现两次，
        # 那么它必将出现在两个不同的后缀中，
        # 因此对后缀数组进行排序，以寻找相同的后缀，
        # 然后扫描数组，比较相邻的元素便可以找出最长的重复子串。

        if not S:
            return ""
        LRS = {}
        for i in range(len(S)):
            LRS[i] = S[i:]
        print(LRS)
        keys = list(LRS.keys())
        keys.sort()

        print(keys)
        maxlen = 0
        for i in range(len(S)-1):
            print(LRS[i], LRS[i+1])
#         做不来了


# GG





str = "banana"
s = Solution()
print(s.longestDupSubstring(str))