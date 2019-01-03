class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def build_dict(str):
            odd = {}
            double = {}
            for i , char in enumerate(str):
                if i % 2 == 0:
                    if char not in double:
                        double[char]= 1
                    else:
                        double[char] += 1
                else:
                    if char not in odd:
                        odd[char] = 1
                    else:
                        odd[char] += 1
            return odd, double

        check_list = [-1 for  _ in range(len(A))]
        save_list = [[] for _ in range(len(A))]
        for index, each in enumerate(A):
            left, right = build_dict(each)
            save_list[index] = [left, right]


        for index, each in enumerate(A):
            if check_list[index] == -1:
                check_list[index] = index
                for i in range(index+1, len(A)):
                    if check_list[i] == -1:
                        print(index, i)
                        if save_list[i] == save_list[index]:
                            check_list[i] = index


        return len(set(check_list))






A  = ["ababaa","aaabaa"]
s = Solution()
print(s.numSpecialEquivGroups(A))