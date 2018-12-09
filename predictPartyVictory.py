class Solution:
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        先对后面的ban，每次结束之后再ban之前的
        """
        Dire_ban = 0
        Radiant_ban = 0

        Ban_list = {}
        act_R = []
        act_D = []

        while(True):
            for index, each in enumerate(senate):
                if index in Ban_list:
                    pass
                else:
                    if each == 'R':
                        if Radiant_ban>0:
                            # Ban_list.append(index)
                            Ban_list[index] = True
                            Radiant_ban -= 1
                        else:
                            Dire_ban += 1
                            act_R.append(index)
                    else:
                        if Dire_ban>0:
                            # Ban_list.append(index)
                            Ban_list[index] = True
                            Dire_ban -=1
                        else:
                            Radiant_ban += 1
                            act_D.append(index)


            # 结束一轮清算前面的
            print(Dire_ban, Radiant_ban, Ban_list)
            if Dire_ban>0:
                if Dire_ban > len(act_D):
                    return "Radiant"
                else:
                    for each_index in act_D[:Dire_ban]:
                        # Ban_list.append(each_index)
                        Ban_list[each_index] = True
            if Radiant_ban>0:
                if Radiant_ban > len(act_R):
                    return "Dire"
                else:
                    for each_index in act_R[:Radiant_ban]:
                        Ban_list[each_index] = True

            act_D = []
            act_R = []
            Dire_ban = 0
            Radiant_ban = 0






t = "RRDDDRDDRDRDRR"
s = Solution()
print(s.predictPartyVictory(t))




