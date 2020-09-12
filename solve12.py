class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        special_case = {4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        normal_case = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        ans = ""
        count = 0
        digit = 1000
        while True:
            if digit == 0:
                break
            now_digit = int(num/digit)
            if now_digit*digit in special_case:
                ans += special_case[now_digit*digit]
            else:
                if 5 <= now_digit:
                    ans += normal_case[5*digit]
                    for i in range(now_digit-5):
                        ans += normal_case[digit]
                else:
                    for i in range(now_digit):
                        ans += normal_case[digit]
            num -= now_digit*digit
            digit = int(digit/10)
            count += 1
        return ans
        