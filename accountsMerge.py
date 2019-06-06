class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        图形的广度优先搜索
        """
        if len(accounts) < 2:
            return accounts

        Account_hash = {}
        number_hash = {}
        name_number = []
        for each in accounts:
            name = each[0]
            name_number.append(name)
            number_hash[len(name_number)] = []
            for each_email in each[1:]:
                print(each_email)
                number_hash[len(name_number)].append(each_email)
                if each_email not in Account_hash:
                    Account_hash[each_email] = [len(name_number)]
                else:
                    Account_hash[each_email].append(len(name_number))
        print(name_number, Account_hash, number_hash)

        number_hash_check = [False for _ in range(len(number_hash))]
        res = []
        used_email = set()
        for i in range(len(number_hash_check)):
            if number_hash_check[i] == False:
                check_name = name_number[i]
                tem = [check_name]
                waiting_list = [i+1]
                while(waiting_list):
                    check_index = waiting_list.pop()
                    number_hash_check[check_index - 1] = False
                    for each_emal in number_hash[check_index]:
                        if each_emal not in used_email:
                            tem.append(each_emal)
                            used_email.add(each_emal)
                            for each_nextindex in Account_hash[each_emal]:
                                if number_hash_check[each_nextindex-1] == False:
                                    waiting_list.append(each_nextindex)
                if len(tem) > 1:
                    tem[1:] = sorted(tem[1:])
                    res.append(tem)
        return res

    def accountsMerge2(self, accounts):
        def mergeAccounts(accounts):
            parent = {}
            for email in accounts[0]:
                parent[email] = accounts[0][0]

            for account in accounts[1:]:
                for email in account:
                    tmp = email
                    if tmp in parent:
                        while parent[tmp] != tmp:
                            tmp = parent[tmp]

                        for i in account:
                            if i in parent:
                                while parent[i] != i:
                                    i = parent[i]
                            parent[i] = tmp
                        break
                    else:
                        parent[tmp] = account[0]

            root_dict = {}
            for email in parent:
                root = email
                while parent[root] != root:
                    root = parent[root]

                if root in root_dict:
                    root_dict[root].append(email)
                else:
                    root_dict[root] = [email]

            merged_emails = []
            for i in root_dict:
                merged_emails.append(root_dict[i])

            return merged_emails

        accout_list = {}
        for accout in accounts:
            user_name = accout[0]
            try:
                accout_list[user_name].append(accout[1:])
            except KeyError:
                accout_list[user_name] = [accout[1:]]

        merged_accouts = []
        for user in accout_list:
            emails = accout_list[user]
            if len(emails) > 1:
                merged_emails = mergeAccounts(emails)
            else:
                merged_emails = emails

            for i in merged_emails:
                x = list(set(i))
                x.sort()
                x.insert(0, user)
                merged_accouts.append(x)

        return merged_accouts


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]


s = Solution()
print(s.accountsMerge(accounts))

accounts =[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(s.accountsMerge(accounts))
