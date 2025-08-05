class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # n = len(s)
        # m = len(t)

        # if len(s)!=len(t):
        #     return False
        
        # countS, countT = {}, {}

        # for i in range(n):
        #     countS[s[i]] = 1 + countS.get(s[i],0) #get(val,defVal) ensures if no occurence it is created and then read
        #     countT[t[i]] = 1 + countT.get(t[i],0)
        
        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False
        
        # return True

        return sorted(s) == sorted(t)