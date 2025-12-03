class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ctr = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                ctr +=1
        return ctr <=1
                
        