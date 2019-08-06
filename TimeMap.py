class TimeMap0:
    # cost too much time
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_for_key = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
            if key not in self.dict_for_key:
                self.dict_for_key[key] = {timestamp: value}

            else:
                self.dict_for_key[key].update({timestamp:value})


    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key not in self.dict_for_key:
            return ""
        else:
            if timestamp in self.dict_for_key[key]:
                return self.dict_for_key[key][timestamp]
            else:
                tem_dict = list(self.dict_for_key[key].keys())
                if len(tem_dict) == 1:
                    return self.dict_for_key[key][tem_dict[0]]
                if tem_dict[0] > timestamp:
                    return ""
                else:
                    start = 0
                    while(start < len(tem_dict)):
                        if tem_dict[start]<timestamp:
                            start += 1
                        else:
                            break
                    if start == len(tem_dict):
                        return self.dict_for_key[key][tem_dict[-1]]
                    return self.dict_for_key[key][tem_dict[start-1]]


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.dict_largest_time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = {timestamp: value}
            self.dict_largest_time[key] = [timestamp]
        else:
            self.dict[key][timestamp] = value
            self.dict_largest_time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        if self.dict_largest_time[key][-1] <= timestamp:
            return self.dict[key][self.dict_largest_time[key][-1]]
        if self.dict_largest_time[key][0] > timestamp:
            return ""

        if self.dict_largest_time[key][0] == timestamp:
            return self.dict[key][self.dict_largest_time[key][0]]

        # //binaray search
        init = 0
        last = len(self.dict_largest_time[key]) - 1
        mid = (init + last) // 2
        while (mid < len(self.dict_largest_time[key]) - 1 and mid > 0):
            if self.dict_largest_time[key][mid] == timestamp:
                return self.dict[key][self.dict_largest_time[key][mid]]
            elif self.dict_largest_time[key][mid + 1] > timestamp:
                break
            else:
                if self.dict_largest_time[key][mid] > timestamp:
                    last = mid - 1
                else:
                    init = mid + 1
            mid = (init + last) // 2
        return self.dict[key][self.dict_largest_time[key][mid]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Your TimeMap object will be instantiated and called as such:
if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo","high",10)
    obj.set("foo","low",20)

    print(obj.get("foo",5))
    print(obj.get("foo",10))
    print(obj.get("foo",15))
    print(obj.get("foo",20))
    print(obj.get("foo",25))




