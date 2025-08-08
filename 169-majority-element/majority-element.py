class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxel = 0

        for i in range(len(nums)):
            if count == 0:
                maxel = nums[i]
                count +=1
            elif nums[i] == maxel:
                count+=1
            else:
                count-=1
        return maxel


        