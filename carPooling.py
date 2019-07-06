class Solution:
    def carPooling(self, trips, capacity) -> bool:
        if not trips:
            return True
        if capacity < 1:
            return False


        trips.sort(key=lambda x:x[1], reverse=False)
        print(trips)

        open_capacity = [capacity] * 1001
        for i in range(1, 1001):
            if open_capacity[i] < 0:
                return False

            if not trips:
                continue
            else:
                if i < trips[0][1]:
                    continue

                while(trips and i == trips[0][1]):
                    for index in range(trips[0][1], trips[0][2]):
                        open_capacity[index] -= trips[0][0]
                        if open_capacity[index] < 0:
                            return False
                    trips.pop(0)
        return True









trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
s = Solution()
print(s.carPooling(trips, capacity))

trips = [[2,1,5],[3,3,7]]
capacity = 5
print(s.carPooling(trips, capacity))

trips = [[2,1,5],[3,5,7]]
capacity = 3
print(s.carPooling(trips, capacity))

trips = [[3,2,7],[3,7,9],[8,3,9]]
capacity = 11
print(s.carPooling(trips, capacity))

trips =[[7,5,6],[6,7,8],[10,1,6]]
capacity = 16
print(s.carPooling(trips, capacity))

trips =[[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]]
capacity = 12
# False
print(s.carPooling(trips, capacity))
