class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_set = set()
        left = 0
        right = 0
        length = 0
        max_length = 0
        if len(s) == 0:
            return 0
        while True:
            if s[right] not in num_set:
                length = right - left + 1
                if max_length < length:
                    max_length = length
                num_set.add(s[right])
                right+=1
            else:
                num_set.remove(s[left])
                left+=1
            if right == len(s):
                break
        return max_length
                    