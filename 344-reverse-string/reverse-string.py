class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        temp = []
        for i in range(len(s)-1,-1,-1):
            temp.append(s[i])
        for j in range(len(s)):
            s[j] = temp[j]
        return s
            

        