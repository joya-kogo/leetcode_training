class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_char = {2:"abc",3:"def",4:"ghi",5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        str_list = []
        for n in digits:
            str_list.append(dig_char[int(n)])
        ans_list = []
        self.dfs(str_list, "", 0, ans_list)
        print(ans_list)
        return ans_list
    
    def dfs(self, str_list, now, idx, ans_list):
        if idx == len(str_list):
            return now
        for c in str_list[idx]:
            # print(c, now, idx)
            ans = self.dfs(str_list, now+c, idx+1, ans_list)
            if len(ans) == len(str_list):
                ans_list.append(ans)
        return now