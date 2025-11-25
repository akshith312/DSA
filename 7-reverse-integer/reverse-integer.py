class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        num = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x!=0:
            rem = x%10
            x = x//10
            num = (num*10) + rem
            if num < -2**31 or num > 2**31 -1:
                return 0
        return (num*sign) 

        