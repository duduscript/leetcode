class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit,m = 0,prices[0]
        for i in xrange(1,len(prices)):
            if prices[i] < m:
                m = prices[i]
            elif prices[i] - m >profit:
                profit = prices[i] - m
        return profit