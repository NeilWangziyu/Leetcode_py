# import sklearn
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import make_moons
# from sklearn.model_selection import train_test_split
# X, y = make_moons(n_samples=100, noise=0.25)
# X_train, X_test,y_train, y_test = train_test_split(X,y,stratify=y)
# print(X_train)

from typing import List

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        res_un = set()
        res_double = set()
        for each in A:
            if each not in res_double:
                if each not in res_un:
                    res_un.add(each)
                else:
                    res_un.remove(each)
                    res_double.add(each)
        if not res_un:
            return -1
        return max(res_un)