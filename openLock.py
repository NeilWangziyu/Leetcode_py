from typing import List
from queue import Queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 我觉得自己的主要问题在于，转换的过程有点慢
        if target == "0000":
            return 0

        deadends = set(deadends)
        # print(deadends)


        check_list = ["0000"]
        c = 0
        while(check_list):
            next_check = []
            # print(len(check_list))
            for each_num in check_list:
                if each_num in deadends:
                    continue
                deadends.add(each_num)
                if each_num == target:
                    return c

                for i in range(4):
                    plus = str((int(each_num[i]) + 1) % 10)

                    minus = (int(each_num[i]) - 1)
                    if minus == -1:
                        minus = "9"
                    else:
                        minus = str(minus)
                    if each_num[:i] + plus + each_num[i+1:] not in deadends:
                        if each_num[:i] + plus + each_num[i+1:] not in deadends:
                            next_check.append(each_num[:i] + plus + each_num[i+1:])
                    if each_num[:i] + minus + each_num[i+1:] not in deadends:
                        if each_num[:i] + minus + each_num[i+1:] not in deadends:
                            next_check.append(each_num[:i] + minus + each_num[i+1:])

            if next_check != []:
                check_list = next_check
                c += 1
            # print(check_list,c)
        return -1



    def openLock2(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)  # in 操作在set中时间复杂度为O(1)
        if '0000' in deadends:
            return -1

        # -------------------------------BFS 开始----------------------------------
        # 初始化根节点
        q = Queue()
        q.put(('0000', 0))  # (当前节点值，转动步数)

        # 开始循环队列
        while not q.empty():

            # 取出一个节点
            node, step = q.get()

            # 放入周围节点
            for i in range(4):
                for add in (1, -1):
                    cur = node[:i] + str((int(node[i]) + add) % 10) + node[i + 1:]
                    if cur == target:
                        return step + 1
                    if not cur in deadends:
                        q.put((cur, step + 1))
                        deadends.add(cur)  # 避免重复搜索
        # -------------------------------------------------------------------------
        return -1



    def openLock3(self, deadends, target):
        # 查看是否有解 ####
        if "0000" in deadends:
            return -1

        lst = []
        for i, n in enumerate(list(target)):
            b = list(target)
            if n == "9":
                b[i] = "0"
            else:
                b[i] = str(int(n) + 1)
            c = "".join(b)
            lst.append(c)
            if n == "0":
                b[i] = "9"
            else:
                b[i] = str(int(n) - 1)
            c = "".join(b)
            lst.append(c)

        dead_flag = True
        for i in lst:
            if i not in deadends:
                dead_flag = False
                break
        if dead_flag:
            return -1
        ###########

        # 计算最小步数
        num = 0
        for i, n in enumerate(target):
            if int(n) > 5:
                num += (10 - int(n))
            else:
                num += int(n)

        # 查看是否能够使用最小步数
        lst2 = set()
        for i, n in enumerate(list(target)):
            b = list(target)
            if int(n) > 5:
                if n == "9":
                    b[i] = "0"
                else:
                    b[i] = str(int(n) + 1)
            else:
                if n == "0":
                    b[i] = "0"
                else:
                    b[i] = str(int(n) - 1)
            c = "".join(b)
            lst2.add(c)

        if target in lst2:
            lst2.remove(target)

        min_flag = False
        for i in lst2:
            if i not in deadends:
                min_flag = True
                break

        return num if min_flag else num + 2

if __name__ == "__main__":
    s = Solution()
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(s.openLock(deadends, target))

    deadends = ["8888"]
    target = "0009"
    print(s.openLock(deadends, target))
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"

    print(s.openLock2(deadends, target))
    # print(s.openLock(deadends, target))



