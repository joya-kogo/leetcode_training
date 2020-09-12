class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if s.count("(") != s.count(")") or s.count("[") != s.count("]") or s.count("{") != s.count("}"):
            return False
        for i in range(len(s)-1):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                poped = stack.pop()
                if (s[i] == ")" and poped == "(") or (s[i] == "}" and poped == "{") or (s[i] == "]" and poped == "["):
                    continue
                else:
                    return False
        return True
                
            