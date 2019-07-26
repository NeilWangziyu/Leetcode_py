from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        check_index = [[-1, -1] for _ in range(26)]
        for i in range(len(S)):
            index = ord(S[i]) - ord("a")
            if check_index[index][0] == -1:
                check_index[index][0] = i
                check_index[index][1] = i
            else:
                check_index[index][1] = i
        res = []
        # print(check_index)
        for each in check_index:
            if each[1] != -1:
                res.append(each)
        res.sort(key=lambda x:x[0])

        # print(res)

        r = []
        for i in range(len(res)):
            if not r:
                r.append(res[i])
            else:
                if res[i][0] > r[-1][1]:
                    r.append(res[i])
                else:
                    r[-1][1] = max(r[-1][1], res[i][1])
        # print(r)
        res_num = []
        for each in r:
            res_num.append(each[1]-each[0]+1)
        return res_num



    def partitionLabels2(self, S: str) -> List[int]:
        ans=[]
        dic={}
        begin=0
        maxend=0
        for i in range(len(S)-1,-1,-1):
            if S[i] not in dic:
                dic[S[i]]=i
        for i in range(len(S)):
            if dic[S[i]]>maxend:
                maxend=dic[S[i]]
            if i==maxend:
                ans.append(maxend-begin+1)
                maxend,begin=i+1,i+1
        return ans




s = Solution()
# S = "ababcbacadefegdehijhklij"

# print(s.partitionLabels(S))
#
# S = "qvmwtmzzse"
# print(s.partitionLabels(S))

S = "caedbdedda"

print(s.partitionLabels(S))
