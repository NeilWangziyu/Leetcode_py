from typing import List
from collections import Counter
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.list = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        temp = self.list[left:right+1]
        dic = Counter(temp)
        for key, val in dic.items():
            if val >= threshold:
                return key
        return -1

    # def query1(self, left: int, right: int, threshold: int) -> int:
    #     超时
    #     select_list = self.list[left:right + 1]
    #     result = select_list[0]
    #     times = 1
    #     for i in range(1, len(select_list)):
    #         if times == 0:
    #             result = select_list[i]
    #             times = 1
    #         else:
    #             if select_list[i] == result:
    #                 times += 1
    #             else:
    #                 times -= 1
    #     all_result = 0
    #     for each in select_list:
    #         if each == result:
    #             all_result += 1
    #     if all_result >= threshold:
    #         return result
    #     else:
    #         return -1

    # def query0(self, left: int, right: int, threshold: int) -> int:
    #     select_list = self.list[left:right+1]
    #     counter = Counter(select_list)
    #     for each in counter.keys():
    #         if counter[each] >= threshold:
    #             return each
    #     return -1





# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)