class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute force
        # count = 0
        # maxel = 0

        # for i in range(len(nums)):
        #     if count == 0:
        #         maxel = nums[i]
        #         count +=1
        #     elif nums[i] == maxel:
        #         count+=1
        #     else:
        #         count-=1
        # return maxel

        count = defaultdict(int) 
        elem = 0
        maxc = 0

        for num in nums:
            count[num]+= 1
            if maxc < count[num]:
                elem = num
                maxc = count[num]
        return elem



        