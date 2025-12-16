class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        hashmap = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in hashmap:
                if res and res[-1] == hashmap[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        if not res:
            return True
        else:
            return False 
        