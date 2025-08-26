class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[(i+k)%n] = nums[i]
        nums[:] = res
        
        