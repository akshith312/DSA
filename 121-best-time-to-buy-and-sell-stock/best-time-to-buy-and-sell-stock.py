class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #brute force
        # maxp = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         maxp = max(maxp, sell - buy)
        # return maxp

        l = 0
        r = 1
        maxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
            r += 1
        return maxp
