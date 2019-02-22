class Solution:
    def splitIntoFibonacci(self, S: 'str') -> 'List[int]':
        """
        回溯算法
        :param S:
        :return:
        """

        if not S:
            return []
        res = []
        def traceback(S, res, index):
            if index == len(S) and len(res) > 2:
                return True
            for i in range(index, len(S)):
                if S[index] == '0' and i > index:
                    break
                num = int(S[index:i+1])
                if num  >= 2**31-1:
                    break

                if len(res) >= 2 and res[-1]+res[-2] < num:
                    break
                if len(res) < 2 or res[-1]+res[-2] == num:
                    res.append(num)
                    if traceback(S, res, i+1):
                        return True
                    res.pop()

            return False

        traceback(S, res, 0)

        return res



S = "123456579"
s = Solution()
print(s.splitIntoFibonacci(S))
