class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """

        if len(tree)<=2:
            return len(tree)
        slow = 0
        quick = 0
        max_fruit = 0

        fruit_have = []
        cur_len = 0
        for i, t in enumerate(tree):
            if t in fruit_have:
                cur_len += 1
                if t == fruit_have[0]:
                    slow = quick
                    quick = i
                    fruit_have = fruit_have[::-1]
            else:
                if len(fruit_have) == 0:
                    fruit_have.append(t)
                    slow = i
                    cur_len = 1
                elif len(fruit_have) == 1:
                    fruit_have.append(t)
                    quick = i
                    cur_len += 1
                else:
                    # now we meet third category of fruit
                    if not max_fruit or cur_len > max_fruit:
                        max_fruit = cur_len
                    cur_len = i - quick + 1
                    slow = quick
                    quick = i
                    fruit_have = [fruit_have[1], t]
        if not max_fruit or cur_len > max_fruit:
            max_fruit = cur_len
        return max_fruit

    def totalFruit2(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        a = tree[0]
        b = -1
        max_len = 0
        cur_len = 0
        for i in range(len(tree)):
            if tree[i] != a and tree[i] != b:
                if b == -1:
                    b = tree[i]
                    cur_len = cur_len + 1
                    continue
                # print tree[i], cur_len
                if cur_len > max_len:
                    max_len = cur_len
                a = tree[i - 1]
                b = tree[i]
                cur_len = 2

                j = i - 2
                while tree[j] == tree[i - 1]:
                    cur_len = cur_len + 1
                    j = j - 1
                continue
            if tree[i] == a or tree[i] == b:
                cur_len = cur_len + 1
                # print tree[i], cur_len,"----",a,b
        if cur_len > max_len:
            max_len = cur_len
        return max_len


if __name__ == "__main__":
    s = Solution()
    tree = [1,2,3,2,2]
    print(s.totalFruit(tree))