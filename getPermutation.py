class Solution:
    def getPermutation0(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def nextPermutation(nums):
            peakInd = len(nums) - 1
            while peakInd > 0 and nums[peakInd] <= nums[peakInd - 1]:
                peakInd -= 1
            peakInd -= 1
            if peakInd >= 0:
                swapInd = peakInd + 1
                while swapInd < len(nums) and nums[swapInd] > nums[peakInd]:
                    swapInd += 1
                swapInd -= 1
                nums[swapInd], nums[peakInd] = nums[peakInd], nums[swapInd]
            left = peakInd + 1
            right = len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums

        check_list = [i + 1 for i in range(n)]
        count = 0
        while count < k - 1:
            check_list = nextPermutation(check_list)
            count += 1
        return "".join(map(str, check_list))

    def getPermutation1(self, n: int, k: int) -> str:
        # 回溯
        ans = []
        def dfs(stack, n, ans):
            if len(ans) == k:
                return
            if len(stack) == n:
                ans.append(stack[:])
                return

            for t in range(1, n + 1):
                if str(t) not in stack:
                    stack.append(str(t))
                    dfs(stack, n, ans)
                    stack.pop()

        dfs([], n, ans)
        fa = ''.join(ans[-1])
        return fa


    def getPermutation2(self, n: int, k: int) -> str:
        chs = [*map(str, range(1, 10))]
        factor = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        k -= 1
        ans = ''
        for i in range(n - 1, -1, -1):
            j, k = divmod(k, factor[i])
            ans += chs.pop(j)
        return ans

    def getPermutation(self, n: int, k: int) -> str:
        # it looks like a math method
        res = ''

        m = [str(x) for x in range(1, n + 1)]

        def all_c(n):
            if n == 1:
                return 1
            return n * all_c(n - 1)

        sum_s = all_c(n)
        # sum_s:total number of permutation

        k = k - 1  # 转换成数组下标
        for i in range(n):
            sum_s = sum_s // (n - i)
            temp = k // sum_s
            res = res + m[temp]
            k = k % sum_s
            m.pop(temp)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(5, 5))