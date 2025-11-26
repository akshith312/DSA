class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # #brute force
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        # # s1 = s[::-1]
        # # s1 = s1.lower()
        
        # # if s == s1:
        # #     return True
        # # return False

        # l = 0
        # r = len(s) -1

        # while l<r:
        #     while l<r and not self.alphaNum(s[l]):
        #         l+=1
        #     while r>l and not self.alphaNum(s[r]):
        #         r-=1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l+=1
        #     r-=1
        # return True


    # def alphaNum(self,c):
    #     return(ord('A') <= ord(c) <= ord('Z') or 
    #             ord('a') <= ord(c) <= ord('z') or
    #             ord('0') <= ord(c) <= ord('9'))
        def revstr(s, start, end):
            if start>end:
                return True
            if s[start]!=s[end]:
                return False
            return revstr(s, start+1, end-1)
        return revstr(s, 0, len(s)-1)


        
            

