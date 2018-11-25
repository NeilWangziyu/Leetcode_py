# 递归定义的二叉树
class ListNode:
    def __init__(self, val, leftChild=None, rightChild=None):
        self.val = val
        self.leftchild = leftChild
        self.rightchild = rightChild


def count_ListNode_Tree(t):
    if not t:
        return 0
    return 1 + count_ListNode_Tree(t.leftchild) + count_ListNode_Tree(t.rightchild)

def Sum_ListNode_Tree(t):
    if not t:
        return 0
    return t.val + Sum_ListNode_Tree(t.leftchild)+Sum_ListNode_Tree(t.rightchild)


def preorder(t):
    if not t:
        return []
    res = []
    res += [t.val]
    if t.leftchild:
        res += preorder(t.leftchild)
    if t.rightchild:
        res += preorder(t.rightchild)
    return res


def midorder(t):
    if not t:
        return None
    res = []
    if t.leftchild:
        res += midorder(t.leftchild)
    res += [t.val]
    if t.rightchild:
        res += midorder(t.rightchild)
    return res


def finalorder(t):
    if not t:
        return None
    res = []
    if t.leftchild:
        res += finalorder(t.leftchild)
    if t.rightchild:
        res += finalorder(t.rightchild)
    res += [t.val]
    return res

def levelorder(t):
#     层次遍历满足先入先出队列
# 深度遍历的运行过程是先进后出的，自然的方法是栈和递归
# 广度遍历的运行过程是先进先出的，自然的方法是队列
    if not t:
        return None
    res = []
    myQueue = [[t]]

    while(myQueue):
        nodes = myQueue.pop(0)
        next_level_nodes = []
        print_level = []
        for node in nodes:
            # print(node.val)
            print_level.append(node.val)
            if node.leftchild:
                next_level_nodes.append(node.leftchild)
            if node.rightchild:
                next_level_nodes.append(node.rightchild)
        if next_level_nodes:
            myQueue.append(next_level_nodes)
        res.append(print_level)
    return res


def insert(t, z):
#     z is a ListNode
    if not t:
        return z
    search = t
    while(search):
        if z.val > search.val:
            p = search
            search = search.rightchild

        else:
            p = search
            search = search.leftchild
    if z.val > p.val:
        p.rightchild = z
    else:
        p.leftchild = z
    return t











if __name__ == '__main__':
    t = ListNode(6, ListNode(4,ListNode(3), ListNode(5)), ListNode(10,ListNode(7), ListNode(15, ListNode(14), ListNode(17))))
    # print(count_ListNode_Tree(t))
    # print(Sum_ListNode_Tree(t))
    # print(preorder(t))
    # print(midorder(t))
    # print(finalorder(t))
    print(levelorder(t))
    t = insert(t, ListNode(2))
    t = insert(t, ListNode(16))
    t = insert(t, ListNode(8))
    print(levelorder(t))
    t = insert(t, ListNode(18))
    print(levelorder(t))
    t = delete(t, 7)
    print(levelorder(t))


