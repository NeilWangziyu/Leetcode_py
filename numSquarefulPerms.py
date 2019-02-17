class Solution:
    def numSquarefulPerms(self, A: 'List[int]') -> 'int':
        def DFS(input, length, c_dict):
            import math
            if len(input) == length:
                res.append(input)
                return
            else:
                for each in c_dict.keys():
                    if c_dict[each] > 0:
                        if not input:
                            c_dict[each] -= 1
                            DFS(input + [each], length, c_dict)
                            c_dict[each] += 1

                        elif math.sqrt((each + input[-1])) % 1 == 0:
                            c_dict[each] -= 1
                            DFS(input+[each], length, c_dict)
                            c_dict[each] += 1
                return


        from collections import Counter
        counter = Counter(A)
        res = []
        DFS([], len(A), counter)
        return len(res)





A = [2,2,2]

s = Solution()
print(s.numSquarefulPerms(A))