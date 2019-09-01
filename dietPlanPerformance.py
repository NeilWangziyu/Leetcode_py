from typing import List
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        i = k
        point = 0
        init_p = sum(calories[:k])
        if init_p > upper:
            point += 1
        elif init_p < lower:
            point -= 1

        while(i < len(calories)):
            init_p += calories[i]
            init_p -= calories[i-k]
            if init_p > upper:
                point += 1
            elif init_p < lower:
                point -= 1

            i += 1
        return point


s = Solution()
print(s.dietPlanPerformance(calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3))
print(s.dietPlanPerformance(calories = [3,2], k = 2, lower = 0, upper = 1))
print(s.dietPlanPerformance(calories = [6,5,0,0], k = 2, lower = 1, upper = 5))
print(s.dietPlanPerformance([6,13,8,7,10,1,12,11], 6, 5, 37))
