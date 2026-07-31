class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = x
        revnum = 0
        while x > 0:
            rem = x % 10
            revnum = revnum*10 + rem
            x = x // 10
        if y == revnum:
            return True
        return False

