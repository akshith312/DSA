class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprof = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         diff = prices[j] - prices[i]
        #         maxprof = max(maxprof, diff)
        # return maxprof

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxprof = max(maxprof,diff)
            else:
                l = r
            r += 1
        return maxprof
