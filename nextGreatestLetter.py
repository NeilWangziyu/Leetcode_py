class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters = sorted(letters + [target])
        print(letters)
        for index, each in enumerate(letters):
            if each == target:
                print(index)
                if index == len(letters) - 1:
                    return letters[0]
                else:
                    return letters[index + 1]

S = Solution()
print(S.nextGreatestLetter(["c","f","j", "b"], "a"))
