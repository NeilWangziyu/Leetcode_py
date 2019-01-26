class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        if len(T) == 1:
            return [0]

        res = [0 for _ in range(len(T))]
        tem_list = [None for _ in range(len(T))]
        for index, each in enumerate(T):
            tem_list[index] = set(range(each + 1, 101))
            if index != 0 and each > T[index - 1]:
                for i in range(index, -1, -1):
                    if res[i] == 0:
                        if each in tem_list[i]:
                            res[i] = index - i
        return res


    def dailyTemperatures2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        稍微进步点了， 吐血
        """
        if not T:
            return []
        if len(T) == 1:
            return [0]
        all_dict = {}
        res = [-1 for _ in range(len(T))]
        for index, each in enumerate(T):
            for every in range(each+1, 101):
                if every not in all_dict:
                    all_dict[every] = [index]
                else:
                    all_dict[every].append(index)
            if each in all_dict:
                for each_index in all_dict[each]:
                    if res[each_index] == -1:
                        res[each_index] = index-each_index
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = 0
        return res


    def dailyTemperatures3(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """


        if not T:
            return []
        if len(T) == 1:
            return [0]
        res_list = [0 for _ in range(len(T))]

        stack = []

        for index, num in enumerate(T):

            while stack and num > T[stack[-1]]:
                res_list[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return res_list







T = [73,74,75,71,69,72,76,73]

s = Solution()
print(s.dailyTemperatures(T))
print(s.dailyTemperatures2(T))
print(s.dailyTemperatures3(T))