class ListNode():
    def __init__(self, index, val):
        self.index = index
        self.val = val

class Solution:
    # JZoffer 59
    def maxSlidingWindow(self, nums, k: int):
        if not nums or len(nums)<k or k<0:
            return []
        start = 1
        end = k + 1
        res = []
        res.append(max(nums[0:k]))
        while(end <= len(nums)):
            res.append(max(nums[start:end]))
            start += 1
            end += 1
        return res


    def maxSlidingWindow2(self, nums, k):
        # 双向队列保存当前窗口中最大的值的数组下标
        # 双向队列中的数从大到小排序，
        if not nums or len(nums)<k or k<0:
            return []
        res = []
        Linedlist = []
        for i in range(0, len(nums)):
            while(Linedlist and Linedlist[-1].val <= nums[i]):
                Linedlist.pop()
            Linedlist.append(ListNode(index=i, val=nums[i]))
            Linedlist = sorted(Linedlist, key=lambda x:x.val, reverse=True)

            if Linedlist[0].index <=i - k:
                Linedlist.pop(0)
            if i-k+1>=0:
                res.append(Linedlist[0].val)
        return res

    def maxSlidingWindow3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        window, res = [], []
        # window 保存着index
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    s = Solution()
    print(s.maxSlidingWindow(nums, k))
    print(s.maxSlidingWindow2(nums, k))
