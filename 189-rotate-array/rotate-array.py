class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #extra space
        # n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     res[(i+k)%n] = nums[i]
        # nums[:] = res
        n = len(nums)
        k = k%n

        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
        
        