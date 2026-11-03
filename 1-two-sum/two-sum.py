class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        hashmap = {}
        res = []
        for i in range(len(nums)):
            diff =  target - nums[i]
            if diff  in hashmap:
                return[i, hashmap[diff]]
            
            hashmap[nums[i]] = i
        return res
