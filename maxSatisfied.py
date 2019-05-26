class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        if not customers:
            return 0
        customers_sum = sum(customers)
        unSatisfied_cus = customers
        for index in range(len(grumpy)):
            if grumpy[index] == 0:
                unSatisfied_cus[index] = 0
        total_unSat = sum(unSatisfied_cus)
        i = X
        init = sum(unSatisfied_cus[:X])
        while(i < len(unSatisfied_cus)):
            this_tem = sum(unSatisfied_cus[i-X+1:i+1])
            init = max(this_tem, init)
            i += 1
        return customers_sum - (total_unSat - init)




    def maxSatisfied2(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        lost_customer = [0] * len(grumpy)
        sum_of_lost = [0] * len(grumpy)
        sum_of_customer = sum(customers)
        if len(customers) == 0:
            return 0
        length = len(customers)
        if X > length:
            return sum(customers)
        for i in range(length):
            lost_customer[i] = grumpy[i] * customers[i]
        sum_of_lost[0] = lost_customer[0]
        for i in range(1, length):
            sum_of_lost[i] = sum_of_lost[i - 1] + lost_customer[i]

        dp_X = [0] * len(grumpy)
        max_value = 0
        for i in range(X):
            dp_X[i] = sum_of_lost[i]
            max_value = max(max_value, dp_X[i])

        for i in range(X, length):
            dp_X[i] = sum_of_lost[i] - sum_of_lost[i - X]
            max_value = max(max_value, dp_X[i])
        return sum_of_customer - sum_of_lost[-1] + max_value



    def maxSatisfied3(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        lost_customer = [0]*len(grumpy)
        sum_of_lost = [0]*len(grumpy)
        sum_of_customer = sum(customers)
        if len(customers)==0:
            return 0
        length = len(customers)
        if X>length:
            return sum(customers)
        for i in range(length):
            lost_customer[i]=grumpy[i]*customers[i]
        sum_of_lost[0]=lost_customer[0]
        for i in range(1,length):
            sum_of_lost[i]=sum_of_lost[i-1]+lost_customer[i]
        dp_X = [0]*len(grumpy)
        for i in range(X):
            dp_X[i]=sum_of_lost[i]
        for i in range(X,length):
            dp_X[i]=sum_of_lost[i]-sum_of_lost[i-X]

        max_value = max(dp_X)
        return sum_of_customer-sum_of_lost[-1]+max_value




customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
s = Solution()
print(s.maxSatisfied(customers, grumpy, X))
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
print(s.maxSatisfied2(customers, grumpy, X))
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
print(s.maxSatisfied3(customers, grumpy, X))


customers =[5,8]
grumpy =[0,1]
X = 1
print(s.maxSatisfied(customers, grumpy, X))
customers =[5,8]
grumpy =[0,1]
X = 1
print(s.maxSatisfied2(customers, grumpy, X))
customers =[5,8]
grumpy =[0,1]
X = 1
print(s.maxSatisfied3(customers, grumpy, X))
