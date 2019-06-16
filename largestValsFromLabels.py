class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        # hashforlabels = {}
        # for i in range(len(values)):
        #     if labels[i] not in hashforlabels:
        #         hashforlabels[labels[i]] = [values[i]]
        #     else:
        #         hashforlabels[labels[i]].append(values[i])
        # for each in hashforlabels.keys():
        #     hashforlabels[each].sort(reverse=True)
        # # print(hashforlabels)
        # hashkeys = list(hashforlabels.keys())
        # hashkeys.sort(key=lambda x:hashforlabels[x][0], reverse=True)
        # # print(hashkeys)
        #
        # res = 0
        # for i in range(num_wanted):
        #     if len(hashforlabels[hashkeys[i]]) <= use_limit:
        #         res += sum(hashforlabels[hashkeys[i]])
        #     else:
        #         res += sum(hashforlabels[hashkeys[i]][:use_limit])
        # return res

        labels_count = {label:0 for label in labels}
        # print(labels_count)
        hash_for_values = {}
        values_index = [[values[i], i] for i in range(len(values))]

        # for i in range(len(values)):
        #     if values[i] not in hash_for_values:
        #         hash_for_values[values[i]] = [labels[i]]
        #     else:
        #         hash_for_values[values[i]].append(labels[i])

        values_index.sort(reverse=True, key=lambda x:x[0])
        count = 0
        res = 0
        for each in values_index:
            each_Value = each[0]
            each_label = labels[each[1]]
            if count < num_wanted:
                if labels_count[each_label] < use_limit:
                    labels_count[each_label] += 1
                    res += each_Value
                    count += 1

        return res





values = [5, 4, 3, 2, 1]
labels = [1, 1, 2, 2, 3]
num_wanted = 3
use_limit = 1
s = Solution()
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))


values = [5,4,3,2,1]
labels = [1,3,3,3,2]
num_wanted = 3
use_limit = 2
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))


values = [9,8,8,7,6]
labels = [0,0,0,1,1]
num_wanted = 3
use_limit = 1
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))

values = [9,8,8,7,6]
labels = [0,0,0,1,1]
num_wanted = 3
use_limit = 2
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))


values = [4,9,1,1,2]
labels = [2,2,1,2,2]
num_wanted = 4
use_limit = 2
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))


