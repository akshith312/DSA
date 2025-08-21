class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #brute force
        # for ptr1 in range(len(numbers)):
        #     for ptr2 in range(1,len(numbers)):
        #         if numbers[ptr1] + numbers[ptr2] == target and ptr1!=ptr2:
        #             return [ptr1+1, ptr2+1]
        # return []
        l = 0
        r = len(numbers) - 1

        while l<r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r-=1
            elif curSum < target:
                l+=1
            else:
                return [l+1,r+1]
        return []