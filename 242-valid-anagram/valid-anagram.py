class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = {}
        map2 = {}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            map1[s[i]] = 1 + map1.get(s[i], 0)
        for j in range(len(t)):
            map2[t[j]] = 1 + map2.get(t[j], 0)
        
        for c in map1:
            if map1[c] != map2.get(c,0):
                return False
        return True
       