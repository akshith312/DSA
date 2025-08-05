class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Submission
        n = len(nums)

        new = set(nums)

        m = len(new)

        if n == m:
            return False
        
        return True
        