class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #brute force
        # res = 0

        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         res = max(res, min(height[i],height[j])*(j-i))
        # return res
        res = 0
        area = 0

        l = 0 
        r = len(height) - 1

        while l < r:
            area = min(height[l],height[r]) * (r-l)
            res = max(res,area)

            if height[l] <= height[r]:
                l=l+1
            else:
                r=r-1
        return res