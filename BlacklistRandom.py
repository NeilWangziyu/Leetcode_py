class Solution:
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.black_list = set(blacklist)
        self.white_list = {}

        c = 0
        for each in range(N):
            if each not in self.black_list:
                self.white_list[c] = each
                c += 1
                self.c = c
        self.n = N
        # print(self.white_list)


def pick(self):
    """
    :rtype: int
    """
    if not self.white_list:
        return None
    import random
    check = random.randint(0, self.c - 1)
    return self.white_list[check]

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
# -----超时
class Solution2:
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.s = N - len(blacklist)
        # 小于s的黑名单元素集合
        b_lt_s = {i for i in blacklist if i < self.s}
        # 大于s的非黑名单元素集合
        w_gt_s = {i for i in range(self.s, N)} - set(blacklist)
        # 做映射，使用zip方便一点
        self.m = {k: v for k,v in zip(b_lt_s, w_gt_s)}

    def pick(self):
        """
        :rtype: int
        """
        import random

        r = random.randint(0, self.s-1)
        return r if r not in self.m else self.m[r]
