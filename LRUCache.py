class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.Cache = []
        self.Dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.Cache:
            key_index = self.Cache.index(key)
            p = self.Cache.pop(key_index)
            self.Cache.insert(0, p)
            # print("get",self.Cache)
            return self.Dict[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print("put",self.Cache)

        if key in self.Cache:
            key_index = self.Cache.index(key)
            p = self.Cache.pop(key_index)
            self.Cache.insert(0, p)
            self.Dict[key] = value
            return None

        if len(self.Cache) < self.capacity:
            self.Dict[key] = value
            self.Cache.insert(0, key)
            return None
        else:
            del_previous = self.Cache.pop()
            print("del", del_previous)
            del self.Dict[del_previous]
            self.Dict[key] = value
            self.Cache.insert(0, key)
            return None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict
# 使用OrderedDict会根据放入元素的先后顺序进行排序
class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.lookup.move_to_end(key)
            return self.lookup[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key] = value
        else:
            if len(self.lookup.keys()) == self.capacity:
                self.lookup.popitem(0)
            self.lookup[key] = value
        self.lookup.move_to_end(key)

