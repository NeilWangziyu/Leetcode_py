class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # length = len(dominoes)
        # L = []
        # R = []
        # for i in range(length):
        #     if dominoes[i] == 'L':
        #         L.append(i)
        #     elif dominoes[i] == 'R':
        #         R.append(i)
        # print(L)
        # print(R)
        # L_index = 0
        # R_index = 0
        # init = 0
        # stage = 0
        # res = list(dominoes)
        # while(L_index < len(L) and R_index<len(R)):
        #     print(L[L_index], R[R_index], init, stage)
        #     if stage == 0:
        #         if L[L_index] < R[R_index]:
        #             for index in range(init, L[L_index]):
        #                 res[index] = 'L'
        #             init = L[L_index]
        #             L_index += 1
        #         elif L[L_index] > R[R_index]:
        #             stage = 1
        #             init = R[R_index]
        #             R_index += 1
        #     elif stage == 1:
        #         if L[L_index] > R[R_index]:
        #             for index in range(init,  R[R_index]):
        #                 res[index] = 'R'
        #             init = R[R_index]
        #             R_index += 1
        #
        #         else:
        #             distance = L[L_index] - init - 1
        #
        #             print(distance)
        #             if distance % 2 == 0:
        #                 for index in range(init+1, init+1+distance//2):
        #                     res[index] = 'R'
        #                 for index in range(init+1+distance//2, L[L_index]):
        #                     res[index] = 'L'
        #             else:
        #                 for index in range(init+1, init+1+distance//2):
        #                     res[index] = 'R'
        #
        #                 for index in range(init+1+distance//2+1, L[L_index]):
        #                     res[index] = 'L'
        #             stage = 0
        #             init = L[L_index]
        #             L_index += 1
        # if L_index == len(L) and R_index == len(R):
        #     if stage == 0:
        #         return res
        #     else:
        #         for index in range(init+1,len(res)):
        #             res[index] = 'R'
        # else:
        #     if stage == 0:
        #         if R_index == len(R):
        #             for index in range(init+1,L[-1]):
        #                 res[index] = 'L'
        #         else:
        #             for index in range(R[R_index]+1, len(res)):
        #                 res[index] = 'R'
        #     else:
        #         if R_index == len(R):
        #
        #
        #     print(res)








dominoes = ".L.R...LR..L.."
s = Solution()
print(s.pushDominoes(dominoes))