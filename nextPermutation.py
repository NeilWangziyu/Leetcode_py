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

    def nextPermutation2(self, nums):
        # write your code here
        peakInd = len(nums) - 1
        while peakInd>0 and nums[peakInd] <= nums[peakInd-1]:
            peakInd -=1
        peakInd -=1
        if peakInd>=0:
            swapInd = peakInd + 1
            while swapInd< len(nums) and nums[swapInd]> nums[peakInd]:
                swapInd +=1
            swapInd -=1
            nums[swapInd],nums[peakInd] = nums[peakInd],nums[swapInd]
        left = peakInd + 1
        right = len(nums) - 1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left +=1
            right -=1
        return

    def nextPermutation3(self, nums: List[int]) -> None:
            cur = len(nums)-1
            while cur>0 and nums[cur-1]>=nums[cur]:
                cur -= 1
            if cur==0:
                nums.sort()
            else:
                start = cur
                cur -= 1
                while start<len(nums)-1 and nums[start+1]>nums[cur]:
                    start += 1
                nums[cur], nums[start] = nums[start], nums[cur]
                t = nums[cur+1:]
                t.sort()
                nums[cur+1:] = t
            return
