class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        leng = 0
        for i in range(len(s)):
            subset = set()
            for j in range(i,len(s)):
                if s[j] in subset:
                    break
                subset.add(s[j])
            leng = max(leng, len(subset))
        return leng
        