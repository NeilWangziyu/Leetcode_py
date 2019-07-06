class Solution:
    def removeDuplicateLetters(self, s):
        from collections import Counter

        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        print(counter)
        mono = []
        seen = set()
        for c in s:
            print(mono)
            if c in seen:
                counter[c] -= 1
            else:
                while mono and c < mono[-1] and counter[mono[-1]] > 1:
                    t = mono.pop()
                    seen.remove(t)
                    counter[t] -= 1
                mono.append(c)
                seen.add(c)

        return ''.join(mono)

    def removeDuplicateLetters2(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters2(suffix.replace(c, ''))
        return ''




str = "cbacdcbc"
s = Solution()
print(s.removeDuplicateLetters(str))
print(s.removeDuplicateLetters2(str))