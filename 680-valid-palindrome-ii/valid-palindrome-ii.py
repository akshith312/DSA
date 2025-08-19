class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #brute force
        # if s == s[::-1]:
        #     return True
        # for i in range(len(s)):
        #     newS = s[:i] + s[i+1:]
        #     if newS == newS[::-1]:
        #         return True
        
        # return False

        l = 0 
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l+1:r+1]
                skipR = s[l:r]

                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l+=1
            r-=1
        return True
        
        