class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for each in moves:
            if each == 'U':
                x += 1
            if each == 'D':
                x -= 1
            if each == "L":
                y += 1
            if each == 'R':
                y -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False





s = Solution()
print(s.judgeCircle("UD"))
