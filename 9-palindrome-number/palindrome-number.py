class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rnum = 0
        y = x
        while x>0:
            rem = x%10
            rnum = (rnum*10) + rem
            x = x//10
        
        if rnum == y:
            return True
        return False
        