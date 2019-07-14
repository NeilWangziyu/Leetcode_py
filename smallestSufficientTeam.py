# not finished
from typing import List
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        if not req_skills:
            return []

        skill_hash = {}
        people_hash = {}
        for each in req_skills:
            skill_hash[each] = []

        for index, skilles in enumerate(people):
            # people_hash[index] = skilles
            for skill in skilles:
                skill_hash[skill].append(index)

        print(skill_hash)




if __name__ == "__main__":
    s = Solution()
    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    print(s.smallestSufficientTeam(req_skills, people))

    req_skills = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
    people = [
        ["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"],
        ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]

    print(s.smallestSufficientTeam(req_skills, people))

# some reference
# # define X first
# # define Y second
# typedef
# pair < int, int > pii;
# int
# dp[62][(1 << 16) + 10];
# int
# last[62][(1 << 16) + 10];
# int
# a[72];
#
#
# class Solution {
# public:
#     vector < int > smallestSufficientTeam(vector < string > & req_skills, vector < vector < string >> & people
#
# ) {
#     int
# cnt = 0;
# map < string, int > M;
# for (auto s:req_skills)
# {
#     M[s] = cnt;
# cnt + +;
# }
# cnt = -1;
# for (auto & v:people)
# {
#     a[++cnt] = 0;
# for (auto & s:v)
# {
# if (!M.count(s)) continue;
# a[cnt] |= (1 << M[s]);
# }
# }
# int
# n = M.size();
# int
# S = (1 << n);
# memset(dp, 0x3f, sizeof(dp));
# dp[0][0] = 0;
# for (int i=0; i < people.size();
# i + +) {
#        // cout << a[i] << endl;
# for (int j=0; j < S; j++)
# {
# if (dp[i][j] + 1 < dp[i + 1][j | a[i]]) {
# last[i+1][j | a[i]]=j;
# dp[i+1][j | a[i]]=min(dp[i+1][j | a[i]], dp[i][j]+1);
# }
# if (dp[i][j] < dp[i + 1][j]) {
# last[i+1][j]=j;
# dp[i+1][j]=min(dp[i+1][j], dp[i][j]);
# }
#
# }
# }
#
# vector < int > ans;
# int
# cur = S - 1;
# for (int i=people.size();
# i >= 1;
# i - -) {
#     int
# ls = last[i][cur];
#
# // cout << i << ' ' << cur << ' ' << ls << endl;
# if (ls != cur)
# ans.push_back(i - 1);
# cur = ls;
# }
# cout << dp[n][S - 1] << endl;
# return ans;
# }
# };