# from https://hujiaweibujidao.github.io/blog/2014/05/09/python-data-structures---c4-trees/
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None, balanceFactor=0):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = balanceFactor       #default new node balance factor is 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
        # 如果是左子节点

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def inorder(self, node):
        if node.leftChild:
            self.inorder(node.leftChild)
        self.print_node(node)
        if node.rightChild:
            self.inorder(node.rightChild)

    def levelorder(self, node):
        nodes = []
        nodes.append(node)
        while len(nodes)>0:
            current_node = nodes.pop(0)
            self.print_node(current_node)
            if current_node.leftChild:
                nodes.append(current_node.leftChild)
            if current_node.rightChild:
                nodes.append(current_node.rightChild)

    def print_node(self, node):
        if node.parent:
            print([node.key, node.payload, node.parent.key])
        else:
            print([node.key, node.payload])

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root  =TreeNode(key,val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if currentNode.key > key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size>1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Errorm, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size -1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self, CurrentNode):
        if CurrentNode.isLeaf():
            if CurrentNode.parent.leftChild==CurrentNode:
                CurrentNode.parent.leftChild = None
            else:
                CurrentNode.parent.rightChild = None
        elif CurrentNode.hasAnyChildren():
            if CurrentNode.hasLeftChild():
                if CurrentNode.isLeftChild():
                    CurrentNode.parent.leftChild = CurrentNode.leftChild
                else:
                    CurrentNode.parent.rightChild = CurrentNode.leftChild
                    CurrentNode.leftChild.parent = CurrentNode.parent
            else:
                if CurrentNode.isLeftChild():
                    CurrentNode.parent.leftChild = CurrentNode.rightChild
                else:
                    CurrentNode.parent.rightChild = CurrentNode.rightChild
                    CurrentNode.rightChild.parent = CurrentNode.parent

    def findSuccessor(self, NodeCurrent):
        succ = None
        if NodeCurrent.hasRightChild():
            succ = self.findMin(NodeCurrent.rightChild)
        #     此时succ一定没有leftchild
        else:
            if NodeCurrent.parent:
                if NodeCurrent.isLeftChild():
                    succ = NodeCurrent.parent
                else:
                    NodeCurrent.parent.rightChild = None
                    succ = self.findSuccessor(NodeCurrent.parent)
                    NodeCurrent.parent.rightChild = NodeCurrent
        return succ

    def findMin(self, NodeCurrent):
        current = NodeCurrent
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = self.findSuccessor(currentNode)
            print("find succ:", succ.payload, succ.key)
            self.spliceOut(succ)
            # 有两个child,直接替换，从而不需要更改
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)

            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


class AVLTree(BinarySearchTree):
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.root.balanceFactor = 0
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):  # rotate left
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):  # rotate right
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild  # deal child
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot  # deal child parent
        newRoot.parent = rotRoot.parent  # deal root parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot  # deal new root right child
        rotRoot.parent = newRoot  # deal old root parent
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


if __name__ == '__main__':
    print('test bst')
    mytree = BinarySearchTree()
    mytree[10]="red"
    mytree[14]="blue"
    mytree[16]="yellow"
    mytree[12]="at"
    mytree[13]='dog'
    mytree[11]='cat'
    mytree.levelorder(mytree.root)
    print('--------------------')
    # print(mytree.get(1))
    # mytree[1] = 'kid'
    # print(mytree.get(1))
    # mytree.levelorder(mytree.root)
    mytree.put(9,'men')
    mytree.put(4,'women')
    mytree.put(7,'kid')
    mytree.put(8,'apple')
    mytree.put(2,'orange')
    mytree.put(1,'juice')
    mytree.put(15,'fly')
    mytree.put(5,'butterfly')

    mytree.levelorder(mytree.root)
    print('--------------------')
    # mytree.delete(2)
    mytree.levelorder(mytree.root)
    print(len(mytree))

    print('--------------------')
    print('--------------------')
    # mytree.delete(5)
    mytree.levelorder(mytree.root)
    print(len(mytree))
    print(mytree.get(8))
    print(mytree[8])
    mytree[18] = 'pig'
    mytree.levelorder(mytree.root)
    print(len(mytree))
    print('--------------------')
    mytree.delete(10)
    mytree.levelorder(mytree.root)
    print(len(mytree))
    # print('test avl')
    # mytree = AVLTree()
    # mytree[5] = "red"
    # mytree[4] = "blue"
    # mytree[6] = "yellow"
    # mytree[2] = "at"
    # mytree[3] = 'dog'
    # mytree[1] = 'cat'
    # mytree.put(0,'men')
    # mytree.put(4,'women')
    # mytree.put(7,'kid')
    # mytree.put(8,'apple')
    # mytree.put(9,'orange')
    # mytree.put(1,'juice')
    # mytree.levelorder(mytree.root)










