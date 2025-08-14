class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute force
        # res = 0
        # store = set(nums)

        # for num in nums:
        #     streak, curr = 0, num

        #     while curr in store:
        #         streak+=1
        #         curr+=1
        #     res = max(res, streak)
        # return res

        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n-1 not in numSet:
                length = 1
                while n+length in numSet:
                    length+=1
                longest = max(longest,length)
        return longest


        