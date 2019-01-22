class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def check_word(a, b):
            len_A = len(a)
            len_B = len(b)
            start_a = 0
            start_b = 0
            while(start_a<len_A and start_b<len_B):
                if a[start_a] == b[start_b]:
                    start_a += 1
                    start_b += 1
                else:
                    start_a += 1
            if start_b != len_B:
                return -1
            else:
                return len(b)





        if not d:
            return None
        if not s:
            return None

        d.sort()
        print(d)
        max = 0
        longest = None
        for each in d:
            if check_word(s, each) > max:

                max = check_word(s, each)
                longest = each


        return longest

s = "abpcplea"
d = ["ale","apple","monkey","plea"]

t = Solution()
print(t.findLongestWord(s, d))