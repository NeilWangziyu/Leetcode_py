class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.length = k
        self.circlarList = []

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.circlarList) == self.length:
            return False
        else:
            self.circlarList.append(value)
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if len(self.circlarList) == 0:
            return False
        else:
            self.circlarList.pop(0)
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if len(self.circlarList) == 0:
            return -1
        else:
            return self.circlarList[0]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if len(self.circlarList) == 0:
            return -1
        else:
            return self.circlarList[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.circlarList) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.circlarList) == self.length

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

class MyCircularQueue2:
    # 设定大小+双指针，确实会好很多
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k + 1
        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): return -1
        else: return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        else: return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear + 1) % self.size == self.front