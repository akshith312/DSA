class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        leng = 0
        # for i in range(len(s)):
        #     subset = set()
        #     for j in range(i, len(s)):
        #         if s[j]  in subset:
        #             break
        #         subset.add(s[j])
        #     leng = max(leng, len(subset))
        # return leng
        l = 0
        subs = set()
        for r in range(len(s)):
            while s[r] in subs:
                subs.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            leng = max(leng, w)
            subs.add(s[r])
        
        return leng
