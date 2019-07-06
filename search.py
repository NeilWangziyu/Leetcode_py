class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0

        total_num = len(nums)
        start = 0
        end = len(nums)-1
        while(start<=end):

            mid = (start + end) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def search2(self, nums, target: int) -> bool:
        """
        区别在于存在重复的元素
        解决的办法只能是对边缘移动一步，直到边缘和中间不在相等或者相遇，这就导致了会有不能切去一半的可能。
        所以最坏情况（比如全部都是一个元素，或者只有一个元素不同于其他元素，而他就在最后一个）就会出现每次移动一步，总共是n步，算法的时间复杂度变成O(n)。
        """
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12],5))

    print(s.search2([2,5,6,0,0,1,2],0))
    print(s.search2([2,5,6,0,0,1,2], target = 3))
