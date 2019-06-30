class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        if candies == 0:
            return [0] * num_people
        if num_people == 1:
            return [candies]

        res = [0] * num_people

        c = 1
        index = 0
        while(candies >= c):
            res[index] += c
            candies -= c
            index += 1
            c += 1
            if index > num_people - 1:
                index = 0

        if candies == 0:
            return res
        else:
            res[index] += candies
            return res




candies = 10
num_people = 3
s = Solution()
print(s.distributeCandies(candies,num_people))
