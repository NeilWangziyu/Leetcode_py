class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_res = ""
        for each in address:
            if each != '.':
                new_res += each
            else:
                new_res += '[.]'
        return new_res