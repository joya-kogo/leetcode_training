class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        # if len(s) % 2 == 0 or len(s) % 2 != 0:
        sd = "#"
        for c in s:
            sd += c
            sd += "#"
        s = sd
        p_arr = [0 for i in range(len(s))]
        max_p_len = 0
        max_p_idx = 0
        ans = ""
        for i in range(len(s)):
            if 1 < max_p_len and i <= max_p_idx + max_p_len:
                p_arr[i] = p_arr[max_p_idx - (i - max_p_idx)]
            left = i
            right = i
            pal_len = 0
            sss = s[i]
            while True:
                left -= 1
                right += 1
                if left < 0 or len(s)-1 < right or s[left] != s[right]:
                    p_arr[i] = pal_len
                    break
                sss = s[left] + sss + s[right]
                if s[left] == s[right]:
                    pal_len += 1
                    if max_p_len < pal_len:
                        max_p_len = pal_len
                        max_p_idx = i
                        ans = sss
            before_plen = pal_len
        print(p_arr)
        ans = ans.replace("#", "")
        print(ans)
        return ans