class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start)!=len(end):
            return False
        i=j=0
        start += "T"
        end += 'T'
        while i <len(start) and j < len(end):
            while start[i] == 'X':
                i += 1
            while end[j] == 'X':
                j += 1

            if start[i] != end[j]:
                return False
            if start[i] == 'R'and i > j:
                return False
            if start[i] == 'L' and i < j:
                return False
            i += 1
            j += 1


        return True



start = "XXRXXLXXXX"
end = "XXXXRXXLXX"

s = Solution()
print(s.canTransform(start, end))