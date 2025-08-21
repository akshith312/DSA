class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ptr1 = 1
        count = 0
        for ptr2 in range(1, len(nums)):
            if nums[ptr2] != nums[ptr2-1]:
                nums[ptr1] = nums[ptr2]
                ptr1+=1
        return ptr1

        
        
        