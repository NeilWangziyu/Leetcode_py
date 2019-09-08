from typing import List
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if not distance:
            return 0
        if start == destination:
            return 0

        total = len(distance)
        l1 = 0
        i = start
        while(i != destination):
            l1 += distance[i]
            i += 1
            i = i % total
        l2 = 0
        j = start - 1
        if j < 0:
            j = total - 1

        while(j != destination - 1):
            # print(j)
            l2 += distance[j]
            j -= 1
            if j < 0:
                if j == destination - 1:
                    break
                j = total - 1
        return min(l1, l2)

s = Solution()

print(s.distanceBetweenBusStops([1,2,3,4],0,1))
print(s.distanceBetweenBusStops([1,2,3,4],0,2))
print(s.distanceBetweenBusStops([1,2,3,4],0,3))

print(s.distanceBetweenBusStops([14,13,4,7,10,17,8,3,2,13],2,9))
# 40

print(s.distanceBetweenBusStops([6,47,48,31,10,27,46,33,52,33,38,25,32,45,36,3,0,33,22,53,8,13,18,1,44,41,14,5,38,25,48],22,0))
