class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i == -1:
            nums.sort()
        else:
            j = len(nums)-1
            while j > i :
                if nums[j] > nums[i]:
                    break
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            tail = nums[i+1:]
            tail.sort()
            for j in range(len(tail)):
                nums[i+j+1] = tail[j]

