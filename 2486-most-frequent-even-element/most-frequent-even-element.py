class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        maxel = -1

        for num in nums:
            if num % 2 == 0:
                count = sum(1 for i in nums if i == num)
                if count > max_count or (count == max_count and num < maxel):
                    max_count = count
                    maxel = num
        return maxel 
        