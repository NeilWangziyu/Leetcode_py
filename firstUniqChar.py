class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}

        for index, each in enumerate(s):
            if each not in s_dict:
                s_dict[each] = [index]
            else:
                s_dict[each].append(index)

        # print(s_dict)
        first = len(s)
        for each in s_dict:
            if len(s_dict[each]) == 1:
                if s_dict[each][0] < first:
                    first = s_dict[each][0]

        if first == len(s):
            return -1
        else:
            return first


s_str = "loveleetcode"
s = Solution()
print(s.firstUniqChar(s_str))
