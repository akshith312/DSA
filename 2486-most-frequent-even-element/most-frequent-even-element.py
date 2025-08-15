class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute force
        # max_count = 0
        # maxel = -1

        # for num in nums:
        #     if num % 2 == 0:
        #         count = sum(1 for i in nums if i == num)
        #         if count > max_count or (count == max_count and num < maxel):
        #             max_count = count
        #             maxel = num
        # return maxel 

        seen = {}

        for item in nums:
            if item % 2 ==0 :
                seen[item] = 1 if item not in seen else seen[item] +1
        max = 0
        output = -1

        for num, count in seen.items():
            if count > max:
                max = count
                output = num
            elif count == max:
                output = min(num, output)
        return output
        