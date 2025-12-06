class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ctr = 0
        res = 0
        for i in range(len(nums)):
            if nums[i]==1:
                ctr +=1
                res = max(res,ctr)
            elif nums[i]!=1:
                ctr = 0
        return res
        