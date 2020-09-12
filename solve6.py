class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0:
            return s
        if numRows == 1:
            return s
        one_term = 2 * numRows - 2
        ans = [[]for i in range(numRows)]
        ans_str = ""
        for i in range(0, len(s), one_term):
            self.create_zig(s, i, numRows,one_term, ans, ans_str)
        for i in range(numRows):
            for j in range(len(ans[i])):
                ans_str += ans[i][j]
        return ans_str
    
    def create_zig(self, s, start, numRows,one_term, ans, ans_str):    
        for i in range(start, start + numRows):
            if i == len(s):
                return
            ans[i%one_term].append(s[i])
        for i in range(start+numRows, start+one_term):
            if i == len(s):
                return
            idx = i - numRows + 1
            ans[start+numRows -1 - idx].append(s[i])
                