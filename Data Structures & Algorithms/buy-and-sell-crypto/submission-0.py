class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        curr = maxprofit = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                curr = prices[r] - prices[l]
            elif prices[l] > prices[r]:
                l = r
            maxprofit = max(curr,maxprofit)
    
        return maxprofit