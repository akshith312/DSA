class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #brute force
        # res = 0

        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum+= nums[j]
        #         if sum == k:
        #             res+=1
        # return res

        res = 0
        curSum = 0
        prefixSum = {0:1}

        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSum.get(diff,0)

            prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
        return res