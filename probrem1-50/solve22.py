class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.gen(n, "", 0, 0, ans)
        return ans
    
    def gen(self, n, now, count_l, count_r, ans):
        if n < count_l or n < count_r:
            return
        if len(now) == 2*n:
            ans.append(now)
            return
        self.gen(n, now+"(", count_l+1, count_r, ans)
        if count_l > count_r:
            self.gen(n, now+")", count_l, count_r+1, ans)