class Solution:
    def findRestaurant(self, list1, list2):
        set1 = {}
        set2 = {}
        for index, each in enumerate(list1):
            set1[each] = index
        for index, each in enumerate(list2):
            set2[each] = index

        overlap = (set(set1.keys()) & set(set2.keys()))
        min_index = float('inf')
        min_item = []
        for each in overlap:
            if set1[each] + set2[each] < min_index:
                min_index = set1[each] + set2[each]
                min_item = [each]
            elif set1[each] + set2[each] == min_index:
                min_item.append(each)
        return min_item





list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

s = Solution()
print(s.findRestaurant(list1, list2))

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
print(s.findRestaurant(list1, list2))
