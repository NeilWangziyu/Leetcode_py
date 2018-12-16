class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) < 3:
            return []
        start_num = S[0]
        start = 0
        count = 0
        res = []
        for index, each in enumerate(S):
            if each == start_num:
                count += 1
            else:
                if count >= 3:
                    res.append([start, index-1])

                if index == len(S) - 1:
                    return res
                else:
                    start_num = S[index]
                    start = index
                    count = 1

        if count >= 3:
            res.append([start, len(S)-1])
        return res









str = "bababbaaab"
s = Solution()
print(s.largeGroupPositions(str))