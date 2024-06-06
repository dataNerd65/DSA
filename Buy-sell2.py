class Solution:
    def MaxProfit(self, prices):
        #This problem is a classic example of a greedy algorithm
        if not prices:
            return 0
        
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)

        return maxProfit
    
soln = Solution()
nums = [7,1,5,3,6,4]
print(soln.MaxProfit(nums))