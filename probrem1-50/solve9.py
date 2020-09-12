class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_num = str(x)
        s = "#"
        for i in range(len(str_num)):
            s+=str_num[i]
            s+="#"
        pivot = len(s)/2
        left = pivot
        right = pivot
        while True:
            if left == 0 and right == len(s) - 1:
                return True
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        