class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        if len(nums) ==4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        nums.sort()
        print(nums)
        res = []
#         固定前两个，然后检查后面的
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i-1]:
                if nums[i] + nums[i+1] +nums[i+2] + nums[i+3]<=target:
                    for j in range(i+1, len(nums) - 2):
                        if j == i+1 or nums[j] != nums[j-1]:
                            # print(i,j)
                            target_tem = target - nums[i] - nums[j]

                            p = j + 1
                            q = len(nums) - 1
                            while(p<q):
                                if nums[p] + nums[q] > target_tem:
                                    q = q - 1
                                elif nums[p] + nums[q] < target_tem:
                                    p = p + 1
                                else:
                                    res.append([nums[i], nums[j], nums[p], nums[q]])
                                    p, q = p+1, q-1
                                    while(p<q and nums[p]==nums[p-1]):
                                        p = p + 1
                                    while(q > p and nums[q]==nums[q+1]):
                                        q = q - 1
        return res

    def fourSum2(self, nums, target):
        """
        method1 112ms 97.93%
        先做排序，选定前两个数后，双指针指向后两个数的可选范围的边界，根据sum与target的关系，移动指针
        trick1: 前两个数在遍历过程中，遇到连续的相同数时跳过
        trick2: 前两个数固定后，将后两个数可选范围内的极值同target比较，极端情况下可以提前终止该轮或者整个循环
        trick3: 每次均求和同target比较计算次数太多，可以事先对target和已确定数做减法替代
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        length = len(nums)

        for i, x in enumerate(nums[:-3]):
            target1 = target - x
            if sum(nums[i:i + 4]) > target:
                break
            elif sum(nums[-3:]) < target1 or (i > 0 and x == nums[i - 1]):
                continue
            for j in range(i + 1, length - 2):
                target2 = target1 - nums[j]
                if nums[j + 1] + nums[j + 2] > target2:
                    break
                elif nums[-2] + nums[-1] < target2 or (j > i + 1 and nums[j] == nums[j - 1]):
                    continue
                k, l = j + 1, length - 1
                while k < l:
                    temp = nums[k] + nums[l]
                    if temp > target2:
                        l -= 1
                    elif temp < target2:
                        k += 1
                    else:
                        res.append([x, nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k, l = k + 1, l - 1
        return res

nums = [-4,-1,-1,0,1,2]
target = -1
#
# nums = [1,0,-1,0,-2,2]
# target = 0

s = Solution()
print(s.fourSum(nums, target))
