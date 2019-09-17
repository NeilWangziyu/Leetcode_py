from typing import List
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if not machines:
            return 0
        total_sum = sum(machines)
        if total_sum % len(machines) != 0:
            return -1
        each_machine = total_sum // len(machines)
        res = 0
        balance = 0
        for j in range(len(machines)):
            balance += machines[j] - each_machine
            res = max(res, abs(balance), machines[j]-each_machine)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findMinMoves([1,0,5]))
    # 3
    print(s.findMinMoves([0, 0, 11, 5]))
    # 8
    print(s.findMinMoves([0,3,0]))
    # 2
    print(s.findMinMoves([9,1,8,8,9]))
    # 4
    print(s.findMinMoves([0,0,11,5]))
    # 8

    # 在把差值数组每一项变为0的操作中，只需要求出其中所需移动衣服最多的洗衣机，就是最少的移动次数。
    #
    # 当diff[i] < 0
    # 时，可以从左右两边的洗衣机获取衣服，取左右中的最大值；
    # 当diff[i] > 0
    # 时，需要把洗衣机的衣服向左右转移，此时移动次数等于diff[i]
    #
    # 我们从左向右依次把差值数组中的每一项变为0：考虑到与该洗衣机非相邻的洗衣机可能需要经过该洗衣机来转移衣服，因此
    # 用balance记录当前洗衣机上所要经过的流量。
    # balance += diff[i];
    # balance < 0
    # 说明需要从右边获取衣服，balance > 0
    # 说明需要向右边转移衣服。
    # 那么该洗衣机上的最大操作数为： max(diff[i], Math.abs(balance))



