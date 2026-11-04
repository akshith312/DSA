class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set(nums)
        longest = 0

        leng = 0
        for r in res:
            if (r-1) not in res:
                leng = 0
                while (r+leng) in res:
                    leng += 1
            longest = max(leng, longest)
        return longest

        