class Solution:


    def longestArithSeqLength2(self, A) :
        '''
        :param A: : List[int]
        :return: -> int
        '''
        if len(A)<=2:
            return len(A)
        list_dic = {}
        length = len(A)
        max_length = 2
        for i in range(length):
            if A[i] not in list_dic:
                list_dic[A[i]]=[i]
            else:
                list_dic[A[i]].append(i)
        print(list_dic)
        dp = [set() for i in range(length)]
        for i in range(length):
            for j in range(i+1,length):
                tmp = A[j]-A[i]
                k = j
                now_length = 2
                if tmp not in dp[j]:
                    dp[j].add(tmp)
                    while k:
                        now_value = A[k]+tmp
                        dp[k].add(tmp)
                        if now_value in list_dic:
                            is_availble = False
                            for value in list_dic[now_value]:
                                if value>k:
                                    k=value
                                    now_length+=1
                                    is_availble=True
                                    break
                            k = k*is_availble
                        else:
                            k = 0
                    max_length = max(max_length,now_length)
            print(dp)
        return max_length


if __name__ == "__main__":
    A = [9,4,7,2,10]
    s = Solution()
    print(s.longestArithSeqLength2(A))