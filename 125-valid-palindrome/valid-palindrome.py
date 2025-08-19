class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        s1 = s[::-1]
        s1 = s1.lower()
        
        if s == s1:
            return True
        return False
        
            

