class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([max(0,prices[i]-prices[i-1]) for i in xrange(1,len(prices))])