class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_num = str(x)
        minus_flag = 0
        if str_num[0] == "-":
            str_num = str_num[1:]
            minus_flag = 1
        str_num = str_num[::-1]
        if minus_flag == 1:
            str_num = "-"+str_num
        ans = int(str_num)
        
        if ans < pow(2, 31) - 1 and pow(-2, 31) < ans :
            return ans
        else:
            return 0