class Solution:
    def findOcurrences(self, text: str, first: str, second: str):

        res = []
        text = text.split(" ")
        for i in range(len(text)-2):
            if text[i] == first and text[i+1]==second:
                res.append(text[i+2])
        return res


s = Solution()
text = "alice is a good girl she is a good student"
first = "a"
second = "good"
print(s.findOcurrences(text, first, second))

text = "we will we will rock you"
first = "we"
second = "will"
print(s.findOcurrences(text, first, second))

text = "we will we"
first = "we"
second = "will"
print(s.findOcurrences(text, first, second))
