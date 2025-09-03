class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #brute force
        # leng = 0
        # for i in range(len(s)):
        #     subset = set()
        #     for j in range(i,len(s)):
        #         if s[j] in subset:
        #             break
        #         subset.add(s[j])
        #     leng = max(leng, len(subset))
        # return leng
        
        charSet = set()
        l = 0
        res = 0 

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
