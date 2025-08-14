class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #brute force
        # n = len(prices)
        # maxProf = 0

        # def helper(start):
        #     profit = 0

        #     for buy in range(start,n):
        #         for sell in range(buy+1,n):
        #             if prices[sell] > prices[buy]:
        #                 curProf = prices[sell] - prices[buy]
        #                 curProf += helper(sell + 1)
        #                 profit = max(curProf, profit)
        #     return profit

        # maxProf = helper(0)
        # return maxProf

        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

