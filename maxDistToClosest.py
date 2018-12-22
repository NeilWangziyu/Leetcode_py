class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        people = []
        span = []
        for index, p in enumerate(seats):
            if p != 0:
                people.append(index)
                if len(people) == 1:
                    span.append(index)
                else:
                    print(index)
                    if (people[-1] - people[-2] - 1)%2==0:
                        span.append((people[-1] - people[-2]-1)//2)
                    else:
                        span.append((people[-1] - people[-2]-1)//2 + 1)

        if people[-1] != len(seats) - 1:
            span.append(len(seats) - people[-1]-1)
        print(span)
        return max(span)

seats =[1,0,0,0,1,0,0]
s = Solution()
print(s.maxDistToClosest(seats=seats))
