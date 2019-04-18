class Solution:
    def shiftingLetters(self, S: str, shifts) -> str:
        c = 0
        for i in range(len(S)-1, -1, -1):
            old = shifts[i]
            shifts[i] = shifts[i] + c
            c += old



        smallest = ord('a') - 1
        biggest = ord('z')
        res = ""
        for index,each in enumerate(list(S)):
            each_num = ord(each)
            each_num += shifts[index] % 26
            if each_num > biggest:
                each_num = smallest + each_num - biggest
            res += chr(each_num)
        print(shifts)
        return res




S = "mkgfzkkuxownxvfvxasy"
shifts = [505870226,437526072,266740649,224336793,532917782,311122363,567754492,595798950,81520022,684110326,137742843,275267355,856903962,148291585,919054234,467541837,622939912,116899933,983296461,536563513]

s = Solution()
print(s.shiftingLetters(S,shifts))

S = "ruu"
shifts = [26,9,17]
print(s.shiftingLetters(S,shifts))

S = "abc"
shifts = [3,5,9]
print(s.shiftingLetters(S,shifts))
