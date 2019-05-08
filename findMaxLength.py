class Solution:
    def findMaxLength(self, nums):
        """
        将原数组的0全部变为-1
        则问题等价于“元素值总和为0的连续数组”
        接着遍历数组 记录当前的前缀和的值
        若该前缀和的值已出现过
        则说明标记中的下标到当前扫描的下标的这段数组的总和值是为0的
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 0
        sum_dict = {}
        sum_num = 0
        for i in range(len(nums)):
            if nums[i] ==0:
                nums[i] = -1

        count = 0
        for index in range(len(nums)):
            sum_num += nums[index]
            if sum_num == 0 and index >= count:
                count = index + 1

            if sum_num not in sum_dict:
                sum_dict[sum_num] = index
                continue

            temp = index - sum_dict[sum_num]
            if temp > count:
                count = temp
        return count





nums = [0,1,0]
s  = Solution()
print(s.findMaxLength(nums))