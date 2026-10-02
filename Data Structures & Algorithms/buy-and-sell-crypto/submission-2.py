class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        l = 0 

        profit = 0 

        for r in range(1,len(prices)):
            
            curr = 0


            if prices[l] > prices[r]:
                l = r
            else: 
                curr = prices[r] - prices[l]
            profit = max(curr,profit)

        return profit