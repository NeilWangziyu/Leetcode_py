class Solution:
    def singleNumber(self, nums):
        res = 0
        for each in nums:
            res = res ^ each
        diffNUm = 1
        while (res & diffNUm == 0):

            diffNUm = diffNUm << 1

        print(diffNUm)
        resultA = 0
        resultB = 0
        for each in nums:
            if diffNUm & each:
                resultA = resultA ^ each
            else:
                resultB = resultB ^ each
        return [resultA, resultB]


    def singleNumber2(self, nums):
        nums.sort()
        stack = [nums[0]]

        for i in range(1, len(nums)):
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(nums[i])
        return stack




if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    s = Solution()
    print(s.singleNumber(nums))
    print(s.singleNumber2(nums))