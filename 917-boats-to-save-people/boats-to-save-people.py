class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        res = 0

        l = 0
        r = len(people) - 1

        while l <= r:
            diff = limit - people[r]
            r = r-1
            res = res+1

            if l<=r and diff >= people[l]:
                l = l+1
        return res 
        