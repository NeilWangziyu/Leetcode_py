class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        主要思路就是把nums里的每个数建树，一共有31位，如果当前位上是0，就往左子树走，如果当前位是1，就往右子树走，
        走完了就记录一下这条路径上的这个数是多少。

        然后再线性扫描数组，用贪心的策略向下遍历树，
        贪心的地方在于，如果当前位上是0，而有右子树，就往右子树走，
        因为这样0和右子树上的1异或可以得到1，反之就往左子树走。

        这种贪心策略的正确性在于，优先保障高位异或得到1。而对于二进制的数来说，
        为了得到更大的异或值，最高位的1的重要性比其他位1更高，比如 1000一定大于0111，
        所以得到的一定会是最大的异或值。
        """
        if not nums:
            return 0
        root = TreeNode(-1)

        for num in nums:
            current_node = root
            for i in range(32):
                # print(num & (1 <<(31 - i)))
                if num & (1 <<(31 - i)) == 0:
                    # 如果当前位与运算的结果是1， 就往左走
                    if not current_node.left:
                        current_node.left = TreeNode(0)
                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = TreeNode(1)
                    current_node = current_node.right
            current_node.left = TreeNode(num)

        res = 0
        for num in nums:
            current_node = root
            for i in range(0, 32):
                if num & (1 <<(31 - i)) == 0:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node = current_node.left
                else:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node = current_node.right

            res = max(res, num ^ current_node.left.val)
        return res



    def findMaximumXOR3(self, nums) -> int:
        answer = 0
        for i in range(30, -1, -1):
            prefixes = {num >> i for num in nums}
            print(prefixes)
            answer = (answer << 1) + any(((answer << 1) + 1) ^ p in prefixes for p in prefixes)
        return answer


    def findMaximumXOR2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        base line
        """
        if not nums:
            return 0
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # print(nums[i] ^ nums[j])
                res = max(res, nums[i] ^ nums[j])
        return res






nums = [3, 10, 5, 25, 2, 8]

s = Solution()
print(s.findMaximumXOR(nums))
print(s.findMaximumXOR2(nums))
print(s.findMaximumXOR3(nums))