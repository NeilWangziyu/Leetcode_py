class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        name_last = 0
        typed_last = 0
        name_check = name[0]
        typed_check = typed[0]
        i = 0
        j = 0
        while (i < len(name) and j < len(typed)):
            if name[i] != typed[j]:
                return False

            while (i < len(name) and name[i] == name_check):
                name_last += 1
                i += 1
            while (j < len(typed) and typed[j] == typed_check):
                typed_last += 1
                j += 1
            if typed_last < name_last:
                return False
            if typed_last > 2 * name_last:
                return False

            name_last = 0
            typed_last = 0
            if i < len(name) and j < len(typed):
                name_check = name[i]
                typed_check = typed[j]
        # print(i, j)
        if name_last == 0 and typed_last == 0:
            if i < len(name) or j < len(typed):
                return False
            else:
                return True

        else:
            if typed_last < name_last or typed_last > 2 * name_last:
                return False
            else:
                return True



    def isLongPressedName2(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)