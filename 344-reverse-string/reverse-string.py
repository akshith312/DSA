class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #brute force
        # temp = []
        # for i in range(len(s)-1,-1,-1):
        #     temp.append(s[i])
        # for j in range(len(s)):
        #     s[j] = temp[j]
        # return s

        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

            

        