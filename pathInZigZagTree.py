import math

class Solution:
    def pathInZigZagTree(self, label: int):
        if label == 1:
            return [1]


        n_floor =int(math.ceil(math.log2(label+1)))

        print(n_floor)

        end_pos = self.num_in_floor(label, n_floor)

        res = [label]
        pos = end_pos
        for i in range(n_floor-1, 0, -1):
            pos = pos //2

            num = self.pos_in_floor(pos, i)
            res.insert(0, num)
        return res

    def num_in_floor(self, num, n_floor):
        floor_start_num = 2 ** (n_floor - 1)
        floor_end_num = 2 ** (n_floor) - 1
        if n_floor % 2:
            pos = floor_end_num - num
        else:
            pos = (num - floor_start_num)
        return pos


    def pos_in_floor(self, pos, n_floor):
        floor_start_num = 2 ** (n_floor - 1)
        floor_end_num = 2 ** (n_floor) - 1
        if n_floor % 2:
            num = floor_end_num - pos
        else:
            num = floor_start_num + pos
        return num





s = Solution()
print(s.pathInZigZagTree(label=14))
print(s.pathInZigZagTree(label=2))
print(s.pathInZigZagTree(label=4))
print(s.pathInZigZagTree(label=16))