class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos_dict = {}
#         0:N, 1:E, 2:S, 3:W
#         make sure when the str is finished, it will remains in pos_dict
        instructions = instructions
        direction = 0
        x = 0
        y = 0
        pos_dict["{}-{}".format(x,y)] = [direction]
        for each in instructions*4:
            if each == 'G':
                if direction == 0:
                    y += 1
                if direction == 1:
                    x += 1
                if direction == 2:
                    y -= 1
                if direction == 3:
                    x -= 1
            elif each == 'L':
                direction -= 1
                if direction == -1:
                    direction = 3
            elif each == 'R':
                direction += 1
                if direction == 4:
                    direction = 0

            loc = "{}-{}".format(x,y)
            if loc not in pos_dict:
                pos_dict[loc] = [direction]
            else:
                if direction in pos_dict[loc]:
                    pass
                else:
                    pos_dict[loc].append(direction)
                # return True

        for each in instructions:
            if each == 'G':
                if direction == 0:
                    y += 1
                if direction == 1:
                    x += 1
                if direction == 2:
                    y -= 1
                if direction == 3:
                    x -= 1
            elif each == 'L':
                direction -= 1
                if direction == -1:
                    direction = 3
            elif each == 'R':
                direction += 1
                if direction == 4:
                    direction = 0

            loc = "{}-{}".format(x,y)
            if loc not in pos_dict:
                return False
        return True



s = Solution()
print(s.isRobotBounded("GL"))