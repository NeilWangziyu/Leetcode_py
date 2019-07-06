class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        """
        这题其实运用了贪心的原理
        :param pushed:
        :param popped:
        :return:
        """
        test_stack = []
        index = 0
        for each in pushed:
            test_stack.append(each)
            while (test_stack and test_stack[-1] == popped[index]):
                test_stack.pop()
                index += 1
        return len(test_stack) == 0


if __name__ == "__main__":
    s = Solution()
    pushed = [1, 2, 4, 4, 5]; popped = [5, 4, 4, 2, 1]
    print(s.validateStackSequences(pushed, popped))