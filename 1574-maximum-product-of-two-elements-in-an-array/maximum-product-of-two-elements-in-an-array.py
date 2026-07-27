class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        fm = nums[n-1]
        sm = nums[n-2]

        return (fm-1)*(sm-1)

