class Solution:
    def carFleet(self, target: 'int', position: 'List[int]', speed: 'List[int]') -> 'int':
        dict = {position[index]:index for index in range(len(position))}
        each_position = list(dict.keys())
        each_position.sort(reverse=True)
        time_init = 0
        count = 0
        for each in each_position:
            distance = target - each
            spe = speed[dict[each]]
            time = distance / spe
            print(spe)
            if time <= time_init:
                continue
            else:
                time_init = time
                count += 1
        print(count)
        return count



target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
s = Solution()
print(s.carFleet(target, position, speed))