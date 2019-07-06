import heapq
from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        dic_of_barcodes = {}
        if len(barcodes)<3:
            return barcodes
        for i in barcodes:
            if i not in dic_of_barcodes:
                dic_of_barcodes[i]=1
            else:
                dic_of_barcodes[i]+=1
        keys = list(dic_of_barcodes.keys())
        keys = sorted(keys,key=lambda i:dic_of_barcodes[i],reverse=True)

        print(keys)

        res = []
        length = len(keys)
        lastnum = -1
        for i in range(len(barcodes)):
            for j in range(2):
                if keys[j] != lastnum:
                    res.append(keys[j])
                    dic_of_barcodes[keys[j]]-=1
                    lastnum=keys[j]
                    break
            if dic_of_barcodes[keys[j]] == 0:
                del keys[j]
                length -= 1
            elif j==length-1 or dic_of_barcodes[keys[j]]>=dic_of_barcodes[keys[j+1]]:
                continue
            else:
                keys[j],keys[j+1]=keys[j+1],keys[j]
        return res

    def rearrangeBarcodes2(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        pq = []
        cnts = Counter(barcodes)
        for key, val in cnts.items():
            heapq.heappush(pq, (-val, key))
        result = []
        while pq:
            _, num = heapq.heappop(pq)
            cnts[num] -= 1
            if not result:
                result.append(num)
            else:
                last = result[-1]
                result.append(num)
                if cnts[last]:
                    heapq.heappush(pq, (-cnts[last], last))
        return result



s = Solution()
print(s.rearrangeBarcodes([1,1,1,2,2,2]))

print(s.rearrangeBarcodes([1,1,1,1,2,2,3,3]))
