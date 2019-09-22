from typing import List
import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # 把所有只连接一个点加入外层洋葱队列（集合），然后一层一层往内剥，直到剩余1或2个点时停止，
        # 这两个点都可以作为树的根节点。

        if n == 1:
            return [0]
        e = collections.defaultdict(set)        #字典初始化为集合
        for i, j in edges:
            e[i] |= {j}                         #把边哈希化，方便调用
            e[j] |= {i}
        print(e)
        q = {i for i in e if len(e[i]) == 1}    #建立初始宽搜队列，长度为1时代表只连接一个点
        while n > 2:
            t = set()                   #临时队列
            for i in q:
                j = e[i].pop()          #把连接点取出
                e[j] -= {i}             #连接是双向的，所以要删除关系
                if len(e[j]) == 1:      #更新后，如果长度为1时则加入下一个轮队列
                    t |= {j}
                n -= 1                  #删除计数
            q = t
        return list(q)




if __name__ == '__main__':
    s = Solution()
    print(s.findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))

    print(s.findMinHeightTrees(n = 6, edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]))

