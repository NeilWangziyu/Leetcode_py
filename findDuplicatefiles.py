class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        if not paths:
            return []
        files = {}
        for each in paths:
            each_list = each.split(' ')
            root_path = each_list[0]
            # print(each_list[1:])
            for each_file in each_list[1:]:
                i = 0
                while(each_file[i] != '('):
                    i += 1
                file_content = each_file[i+1:-1]
                file_root = root_path +'/'+ each_file[:i]
                if file_content not in files:
                    files[file_content] = [file_root]
                else:
                    files[file_content].append(file_root)
        res = []
        for each in files.keys():
            if len(files[each]) > 1:
                res.append(files[each])
        return res

    def findDuplicate2(self, paths):
        d = {}
        for i in paths:
            path = i.split()[0]
            for j in i.split()[1:]:
                left = j.find("(")
                right = j.find(")")
                name = j[0:left]
                content = j[left + 1:right]
                if content not in d:
                    d[content] = [path + '/' + name]
                else:
                    d[content].append(path + '/' + name)
        return [x for x in d.values() if len(x) > 1]


paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]


s = Solution()
print(s.findDuplicate(paths))

# [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

