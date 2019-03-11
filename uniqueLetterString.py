class Solution:
    def uniqueLetterString(self, S: str) -> int:
        """
        预处理每个位置 i，左边第一个和自己一样字符的位置 left，右边第一个和自己一样字符的位置 right。该位置 i 贡献的答案就是 (i - left) * (right - i)。
        对每个位置进行统计。
        """
        cur = [-1 for _ in range(128)]
        pre = [-1 for _ in range(128)]
        i = 0
        res = 0
        while (i < len(S)):
            c = ord(S[i])

            res += (i - cur[c]) * (cur[c] - pre[c])
            pre[c] = cur[c]
            cur[c] = i
            i += 1
        c = ord('A')
        while (c <= ord('Z')):
            res += (i - cur[c]) * (cur[c] - pre[c])
            c += 1

        print(cur)
        print(pre)
        return res % 1000000007

if __name__ == "__main__":
    s = Solution()
    S = 'ABC'
    print(s.uniqueLetterString(S))