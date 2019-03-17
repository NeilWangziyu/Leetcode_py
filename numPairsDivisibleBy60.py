class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        """
        no ac
        :param time:
        :return:
        """
        res = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    res += 1
        return res

    def numPairsDivisibleBy602(self, time) -> int:
        res = 0
        Hash_map_one = {}
        for index, each in enumerate(time):
            left = each % 60
            if left not in Hash_map_one:
                Hash_map_one[left] = [index]
            else:
                Hash_map_one[left].append(index)
        print(Hash_map_one)
        for each in time:
            left_this = each % 60
            left_find = 60 - left_this
            if left_find == 60:
                left_find = 0
            if left_this == left_find:
                if left_find in Hash_map_one:
                    res += (len(Hash_map_one[left_find]) - 1)
            else:
                if left_find in  Hash_map_one:
                    res += (len(Hash_map_one[left_find]))

        return res//2



s = Solution()
TIME =[60,60,60]
print(s.numPairsDivisibleBy602(TIME))