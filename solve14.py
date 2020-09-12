class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        length = 10000000
        for s in strs:
            if len(s) < length:
                length = len(s)
        ans = ""
        final_ans = ""
        for i in range(length):
            now = strs[0][i]
            for j in range(len(strs)):
                if now != strs[j][i]:
                    ans = ""
                    return final_ans
                if j == len(strs) - 1:
                    ans += now
                    if len(final_ans) < len(ans):
                        final_ans = ans
        return final_ans