class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        idx = 0
        while idx != len(s):
            if 1 <= idx and roman[s[idx-1]] < roman[s[idx]]:
                ans -= roman[s[idx-1]]
                ans += (roman[s[idx]]-roman[s[idx-1]])
                idx += 1
            else:
                ans += roman[s[idx]]
                idx += 1
        return ans