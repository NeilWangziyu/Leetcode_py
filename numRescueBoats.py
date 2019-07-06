class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people:
            return 0
        people.sort(reverse=True)
        res = 0

        while (people):
            people_in = people.pop(0)
            if not people:
                res += 1
                continue

            if people_in == limit:
                res += 1
                continue

            left = limit - people_in
            i = 0
            while (True):
                if people[i] <= left:
                    left -= people[i]
                    people.pop(i)
                    break
                else:
                    i += 1

                if i >= len(people):
                    break
            res += 1
        return res

    def numRescueBoats2(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        low = 0
        high = len(people) - 1
        boat = 0
        while(low <= high):
            if people[low] + people[high] <= limit:
                low += 1
            high -= 1
            boat += 1
        return boat

if __name__ == "__main__":
    s = Solution()
    people =[]
    limit = 2
    print(s.numRescueBoats(people, limit))