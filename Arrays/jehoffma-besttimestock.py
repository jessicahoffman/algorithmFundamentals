class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        runningMin = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > runningMin:
                maxProfit = max(maxProfit, prices[i]-runningMin)
            elif prices[i] < runningMin:
                runningMin = prices[i]
        return maxProfit
