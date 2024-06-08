class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        #To store maximum profit calculated so far
        min_price =float('inf')
        #min_price keeps track of the minimum price encountered so far while iterating through the prices
        max_profit = 0 
        #To store maximum profit calculated so far
      
        #iterating through the list

        #For each price update 'min_price'
        for price in prices:
            #if current price is lower than min_price
            if price < min_price:
                min_price = price
            potential_profit = price - min_price

            if potential_profit > max_profit:
                max_profit = potential_profit
        

        #After iterating through the list, 'max_profit' will contain the maximum profit possible
        #if no profit made(prices are in descending order) 'max_profit' will remain 0
        return max_profit
    
soln = Solution()
prices = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print(soln.maxProfit(prices))
print(soln.maxProfit(prices2))

