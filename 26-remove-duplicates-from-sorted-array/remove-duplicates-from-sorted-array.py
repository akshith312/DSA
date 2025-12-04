class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ptr1 = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[ptr1-1]:
                nums[ptr1] = nums[i]
                ptr1+=1
        return ptr1     
        
        
        
        