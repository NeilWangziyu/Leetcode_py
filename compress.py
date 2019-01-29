class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        if len(chars) == 1:
            return 1
        index = 0
        count = 1
        while (index < len(chars)-1):
            if chars[index] == chars[index + 1]:
                count += 1
                chars.pop(index + 1)

            else:
                if count > 1:
                    num = list(str(count))
                    for each in num:
                        chars.insert(index+1, each)
                        index += 1
                    index += 1
                    count = 1
                else:
                    index += 1

        if count == 1:
            return index+1
        else:
            num = list(str(count))
            for each in num:
                chars.insert(index+1, each)
                index += 1
            index += 1

            return index


chars = ["a","b","c"]


s = Solution()
index = s.compress(chars)
print(chars[:index])