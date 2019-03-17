class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        def check(mid):
            time = 0
            this_load = 0
            i = 0
            while(i < len(weights)):
                if weights[i] > mid:
                    return False
                this_load += weights[i]
                if this_load > mid:
                    time += 1
                    this_load = 0
                else:
                    i += 1
            if this_load != 0:
                time += 1


            if time > D:
                return False
            else:
                return True

        low = 1
        high = 50001
        while(low < high):
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low




if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    D = 5

    s = Solution()
    print(s.shipWithinDays(weights, D))