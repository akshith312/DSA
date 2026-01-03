class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Brute Force
        # for i in range(len(nums)):
        #     ctr = 0
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = 1 + hashmap.get(nums[i],0)
        return False
        