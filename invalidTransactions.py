from typing import List
class Solution:
    # def invalidTransactions(self, transactions: List[str]) -> List[str]:
    #     # wrong
    #     if not transactions:
    #         return transactions
    #     transaction_dict = {}
    #     for each_trans in transactions:
    #         each_trans_list = each_trans.split(",")
    #         name = each_trans_list[0]
    #         time = int(each_trans_list[1])
    #         amount = int(each_trans_list[2])
    #         city = each_trans_list[3]
    #         if name not in transaction_dict:
    #             if amount > 1000:
    #                 transaction_dict[name] = [[time, amount,city, False]]
    #             else:
    #                 transaction_dict[name] = [[time, amount,city, True]]
    #         else:
    #             if amount > 1000:
    #                 transaction_dict[name].append([time, amount, city, False])
    #             else:
    #                 transaction_dict[name].append([time, amount, city, True])
    #
    #     res = []
    #
    #     for each_people in transaction_dict.keys():
    #         people_trans = transaction_dict[each_people]
    #         people_trans.sort(key=lambda x:x[0])
    #         for i in range(len(people_trans)):
    #             if people_trans[i][3] == False:
    #                 continue
    #             if i > 0:
    #                 if people_trans[i][0] - people_trans[i-1][0] <= 60 and people_trans[i][2] != people_trans[i-1][2]:
    #                     people_trans[i][3] = False
    #                     people_trans[i-1][3] = False
    #             if i < len(people_trans)-1:
    #                 if people_trans[i+1][0] - people_trans[i][0] <= 60 and people_trans[i][2] != people_trans[i+1][2]:
    #                     people_trans[i][3] = False
    #                     people_trans[i+1][3] = False
    #
    #         for j in range(len(people_trans)):
    #             if people_trans[j][3] == False:
    #                 res.append(",".join([each_people, str(people_trans[j][0]), str(people_trans[j][1]), people_trans[j][2]]))
    #
    #     return res

    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        ts = []
        for t in transactions:
            name, stamp, amount, city = t.split(',')
            stamp = int(stamp)
            amount = int(amount)
            ts.append([name, stamp, amount, city, t])
        ans = set()
        for t in ts:
            if t[2] > 1000:
                ans.add(t[4])
            for o in ts:
                if t[0] == o[0] and abs(t[1] - o[1]) <= 60 and t[3] != o[3]:
                    ans.add(t[4])
        return list(ans)


transactions = ["alice,20,800,mtv", "alice,50,1200,mtv"]
s = Solution()
print(s.invalidTransactions(transactions))

transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
print(s.invalidTransactions(transactions))

transactions =["alice,20,800,mtv","alice,50,100,beijing"]
print(s.invalidTransactions(transactions))

transactions = ["alex,676,260,bangkok","bob,656,1366,bangkok","alex,393,616,bangkok","bob,820,990,amsterdam","alex,596,1390,amsterdam"]
print(s.invalidTransactions(transactions))

transactions = ["bob,649,842,prague","alex,175,1127,mexico","iris,164,119,paris","lee,991,1570,mexico","lee,895,1876,taipei","iris,716,754,moscow",
                "chalicefy,19,592,singapore","chalicefy,820,71,newdelhi","maybe,231,1790,paris","lee,158,987,mexico","chalicefy,415,22,montreal","iris,803,691,milan","xnova,786,804,guangzhou",
                "lee,734,1915,prague","bob,836,1904,dubai","iris,666,231,chicago","iris,677,1451,milan","maybe,860,517,toronto","iris,344,1452,bangkok","lee,664,463,frankfurt","chalicefy,95,1222,montreal",
                "lee,293,1102,istanbul","maybe,874,36,hongkong","maybe,457,1802,montreal","xnova,535,270,munich","iris,39,264,istanbul","chalicefy,548,363,barcelona","lee,373,184,munich","xnova,405,957,mexico",
                "chalicefy,517,266,luxembourg","iris,25,657,singapore","bob,688,451,beijing","bob,263,1258,tokyo","maybe,140,222,amsterdam","xnova,852,330,barcelona","xnova,589,837,budapest","lee,152,981,mexico",
                "alex,893,1976,shenzhen","xnova,560,825,prague","chalicefy,283,399,zurich","iris,967,1119,guangzhou","alex,924,223,milan","chalicefy,212,1865,chicago","alex,443,537,taipei","maybe,390,5,shanghai","bob,510,1923,madrid",
                "bob,798,343,hongkong","iris,643,1703,madrid","bob,478,928,barcelona","maybe,75,1980,shanghai","xnova,293,24,newdelhi","iris,176,268,milan","alex,783,81,moscow","maybe,560,587,milan","alex,406,776,istanbul","lee,558,727,paris",
                "maybe,481,1504,munich","maybe,685,602,madrid","iris,678,788,madrid","xnova,704,274,newdelhi","chalicefy,36,1984,paris","iris,749,200,amsterdam","lee,21,119,taipei","iris,406,433,bangkok","bob,777,542,taipei",
                "maybe,230,1434,barcelona","iris,420,1818,zurich","lee,622,194,amsterdam","maybe,545,608,shanghai","xnova,201,1375,madrid","lee,432,520,dubai","bob,150,1634,singapore","maybe,467,1178,munich","iris,45,904,beijing",
                "maybe,607,1953,tokyo","bob,901,815,tokyo","maybe,636,558,milan","bob,568,1674,toronto","iris,825,484,madrid","iris,951,930,dubai","bob,465,1080,taipei","bob,337,593,chicago","chalicefy,16,176,rome","chalicefy,671,583,singapore",
                "iris,268,391,chicago","xnova,836,153,jakarta","bob,436,530,warsaw","alex,354,1328,luxembourg","iris,928,1565,paris","xnova,627,834,budapest","xnova,640,513,jakarta","alex,119,16,toronto","xnova,443,1687,taipei","chalicefy,867,1520,montreal",
                "alex,456,889,newdelhi","lee,166,3,madrid","bob,65,1559,zurich","alex,628,861,moscow","maybe,668,572,mexico","bob,402,922,montreal"]
print(s.invalidTransactions(transactions))
