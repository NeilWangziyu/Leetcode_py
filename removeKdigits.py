class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return "0"
        if len(num) == k:
            return "0"

        # make sure stack is upgrading
        # stack = list(map(int, list(num)))
        stack = list(num)
        j = 0
        for _ in range(k):
            while(j < len(stack)-1 and stack[j] <= stack[j+1]):
                j += 1
            x = stack.pop(j)
            print("pop", x)
            j = max(0, j-1)
        print(stack)
        nums = "".join(stack)
        if nums.lstrip('0'):
            return nums.lstrip('0')
        else:
            return "0"


    def removeKdigits2(self, num: str, k: int) -> str:
        if not num:
            return "0"
        if len(num) == k:
            return "0"
        num = list(num)
        stack = []
        for each in num:
            while(stack and stack[-1] > each and k):
                stack.pop()
                k -= 1

            stack.append(each)

        while(k):
            stack.pop(-1)
            k -= 1
        # print(stack)
        nums = "".join(stack)
        if nums.lstrip('0'):
            return nums.lstrip('0')
        else:
            return "0"


s = Solution()
print(s.removeKdigits(num = "112", k = 1))
print(s.removeKdigits2(num = "112", k = 1))