class Solution:
    def maxProfit(self, prices):
        total_profit = 0#This variable will keep track of the total profit made
        
        
        """This method then iterates over the prices list starting from the second element(index 1)
        For each price, it checks if the current price is greater than the previous days price
        if the current price is greater, it means that buying the stock on the previous day and
        selling it on the current day would yield a profit. This profit (current price - previous price) is addedto total_profit"""
        for i in range(1, len(prices)):
            if prices[i] > prices[i -1]:
                total_profit += prices[i] - prices[i-1]
        return total_profit
    
soln = Solution()
nums = [7,1,5,3,6,4]

print(soln.maxProfit(nums))