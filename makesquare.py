class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        这种解法，时间过久
        """
        def DFS(square, index, final, each_line):
            if index == final:
                if square[0] == each_line and square[1] == each_line and square[2] == each_line and square[3] == each_line:
                    return True
                else:
                    return False
            for i in range(len(square)):
                if square[i] + nums[index] <= each_line:
                    square[i] = square[i] + nums[index]
                    if DFS(square, index + 1, final, each_line):
                        return True
                    else:
                        square[i] = square[i] - nums[index]
            return False

        if not nums:
            return False
        total = sum(nums)
        if total % 4 != 0:
            return False
        each_line = total // 4
        square = [0, 0, 0, 0]
        nums.reverse()
        # print(nums)
        final = len(nums)
        return DFS(square, 0, final, each_line)



    def makesquares(self, nums):
        total, n = sum(nums), len(nums)
        if total % 4 != 0 or n < 4: return False
        target = total / 4
        nums.sort(reverse=True)  # 降序排序
        used = [False] * n  # 记录

        def dfs(i, tar):  # 判断数字 i, 是否可以组成长为tar， 的边
            if i >= n: return tar % target == 0
            if used[i]: return dfs(i + 1, tar)  # 当前位置已经使用，跳到下个位置
            used[i] = True  # 位置 i 的值没有过，现在使用
            if nums[i] == tar: return True
            if nums[i] < tar:
                tar -= nums[i]
                not_used = [j for j in range(i + 1, n) if not used[j]]  # 记录没有使用过的位置
                for x in not_used:
                    if dfs(x, tar):
                        return True
            used[i] = False  # 恢复未使用状态
            return False

        for i in range(n):  # 遍历所有元素，确保每一个元素都可以分配边
            if not dfs(i, target): return False
        return True


# num =[1,1,2,2,2,4,4,4,4,1,1,1,1]
# num = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
num = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
s = Solution()
print(s.makesquares(num))