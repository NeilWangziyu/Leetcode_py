class TimeMap:

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




