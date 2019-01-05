class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        if not  cpdomains:
            return []
        dict_address = {}
        for each in cpdomains:
            each_list = (each.split(' '))
            num = int(each_list[0])
            # print(num)
            address_list = each_list[1].split('.')
            tem = ""
            while(address_list):
                tem =  address_list.pop() + '.' + tem
                # print(tem, num)
                if tem not in dict_address:
                    dict_address[tem] = num
                else:
                    dict_address[tem] += num
        res = []
        for each in dict_address.keys():
            res.append(str(dict_address[each]) + ' ' + each[:-1])
        return res




cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
s = Solution()
print(s.subdomainVisits(cpdomains))