class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        longest = 0

        for n in numset:
            if (n - 1) not in numset:
                leng = 0
                while (n + leng) in numset:
                    leng += 1
                longest = max(leng, longest)
        return longest