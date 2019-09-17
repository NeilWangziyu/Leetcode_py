class Solution:
    def findSubstring(self, s, words):
        """
        做不来
        :param s:
        :param words:
        :return:
        """
        if not s or not words:
            return []

        lenth = len(words[0]) * len(words)
        word_len = len(words[0])
        from collections import Counter
        words_hash = Counter(words)
        res = []
        for i in range(0, len(s) - lenth + 1):
            tmp = s[i:i + lenth]
            # print(tmp)
            c_tmp = []
            for j in range(0, lenth, word_len):
                c_tmp.append(tmp[j:j+word_len])
            # print(c_tmp)
            c_tem_hash = Counter(c_tmp)
            if c_tem_hash == words_hash:
                res.append(i)
        return res



if __name__ == "__main__":
    str = "barfoothefoobarman"
    words = ["foo", "bar"]
    s = Solution()
    print(s.findSubstring(str, words))
