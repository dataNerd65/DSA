class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price =float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            potential_profit = price - min_price

            if potential_profit > max_profit:
                max_profit = potential_profit

        return max_profit
    
soln = Solution()
prices = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print(soln.maxProfit(prices))
print(soln.maxProfit(prices2))