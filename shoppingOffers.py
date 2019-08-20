from typing import List
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        def shopping(special, needs):  # 从special里刚好购买needs所需的最低花费
            if not sum(needs):  # needs已没有
                return 0
            # 先过滤掉special里已经有某一种物品超过了needs的礼包
            special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(l)), special))
            if not special:  # 如果过滤后为空，那么返回直接以单品购买needs的价格
                return sum(needs[i]*price[i] for i in range(l))
            res = []
            for pac in special:  # 回溯，收集本次购买每种礼包的花费加上若购买该礼包后剩余needs递归的最低花费
                res.append(pac[-1]+shopping(special, [needs[i]-pac[i] for i in range(l)]))
            return min(res)  # 返回本次购买的几种选择中的最低花费

        l = len(price)
        # 先过滤掉不比原价买划算的礼包
        special = list(filter(lambda x: x[-1] < sum(x[i]*price[i] for i in range(l)), special))
        # print(special)
        return shopping(special, needs)

    def shoppingOffers2(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dfs(special, needs):
            s = []
            for spe in special:
                flag = True
                for i in range(len(price)):
                    if spe[i] > needs[i]:
                        flag = False
                        break
                if flag:
                    s.append(spe)
            if len(s) == 0:
                return sum([needs[i] * price[i] for i in range(len(price))])

            r = []
            for spe in s:
                n = [needs[i] - spe[i] for i in range(len(price))]
                r.append(spe[-1] + dfs(s, n))
            return min(r)

        s = []
        for spe in special:
            p = 0
            for i in range(len(price)):
                p += spe[i] * price[i]
            if p > spe[-1]:
                s.append(spe)

        return dfs(s, needs)


s = Solution()
price = [2, 5]
special = [[3, 0, 5], [1, 2, 10]]
needs = [3, 2]
print(s.shoppingOffers(price, special, needs))

price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]
print(s.shoppingOffers(price, special, needs))