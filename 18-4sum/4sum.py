class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #brute force
        # nums.sort()
        # res = set()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             for l in range(k+1, len(nums)):
        #                 if nums[i]+nums[j]+nums[k]+nums[l] == target:
        #                     tmp = [nums[i],nums[j], nums[k], nums[l]]
        #                     res.add(tuple(tmp))
        # return [list(i) for i in res]
        
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n):

                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = n-1             

                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fourSum > target:
                        r-=1
                    elif fourSum < target:
                        l+=1
                    if fourSum == target:
                        res.append([nums[i],nums[j], nums[l], nums[r]])
                        l+=1
                        r-=1

                        while nums[l] == nums[l-1] and l<r:
                            l+=1
                        while nums[r] == nums[r+1] and l<r:
                            r-=1
        return res
