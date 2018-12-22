class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S_list = []
        for each in S:
            if each != "#":
                S_list.append(each)
            else:
                if S_list:
                    S_list.pop()
        T_list = []
        for each in T:
            if each != "#":
                T_list.append(each)
            else:
                if T_list:
                    T_list.pop()

        if len(T_list) != len(S_list):
            return False
        else:
            for i in range(len(T_list)):
                if T_list[i] != S_list[i]:
                    return False
        return True
