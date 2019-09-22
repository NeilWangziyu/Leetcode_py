from typing import List
class Solution:
    def func(self, x, y):
        # True:x > y
        # False:x =< y
        if x+y > y+x:
            return True
        else:
            return False

    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str, nums))
        res_list = self.core(nums)
        return "".join(res_list)


    def core(self, nums):
        if not nums or len(nums) == 1:
            return nums
        anchor = nums[0]
        less = []
        more = []
        for each in nums[1:]:
            if self.func(anchor, each):
                more.append(each)
            else:
                less.append(each)
        return self.core(less) + [anchor] + self.core(more)



if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([3,30,34,9,5]))





