class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """

        while n < 101:
            x = n
            prod = 1

            while x>0:
                rem = x %10
                prod *= rem
                if prod % t == 0:
                    return n
                x = x//10
            n += 1
        return 0

        



        