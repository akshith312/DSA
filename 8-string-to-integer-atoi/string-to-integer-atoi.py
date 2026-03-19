class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.lstrip()

        if not s:
            return 0
        if len(s)==1 and not s[0].isdigit():
            return 0
        
        i = 0
        sign = 1
        if s[i] == '+':
            i+=1
        if s[i] == '-':
            i+=1
            sign = -1
        if i == 2:
            return 0
        
        parsed = 0
        while i < len(s):
            cur = s[i]

            if not cur.isdigit():
                break
            else:
                parsed = (parsed*10) + int(cur)
            i+=1
        
        parsed *= sign

        if parsed > 2**31 - 1:
            return 2**31 - 1
        elif parsed <= -2**31:
            return -2**31
        else:
            return parsed


        