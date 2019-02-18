class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) < 2:
            return 0
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                tem = set(words[j])
                flag = True
                for c_i in set(words[i]):
                    if c_i in tem:
                        flag = False
                if flag:
                    res = max(res, len(words[i])*len(words[j]))
        return res

    def maxProduct2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        h = [0 for _ in range(n)]
        m = 0
        for i in range(n):
            for c in words[i]:
                # 1 左移几位
                h[i] = 1 << (ord(c) - ord('a')) | h[i]


        for i in range(n - 1):
            for j in range(i + 1, n):
                if h[i] & h[j] == 0:
                    m = max(len(words[i]) * len(words[j]), m)
        return m


words = ["a","ab","abc","d","cd","bcd","abcd"]
s = Solution()
print(s.maxProduct(words=words))
print(s.maxProduct2(words=words))