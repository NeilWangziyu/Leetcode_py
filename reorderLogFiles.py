class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        dig = []
        letter = {}
        for each in logs:
            if each.split()[1].isdigit():
                dig.append(each)
            else:
                letter[each.split(' ', 1)[1]] = each.split()[0]
        res_alph = []
        for each in sorted(letter.keys()):
            res_alph.append(letter[each] + " " + each)
        return res_alph + dig






logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
s = Solution()
print(s.reorderLogFiles(logs))