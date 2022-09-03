# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
# main goal is to find maximum value of profit = (current price - buy)
# buy is the min value so far in the prices array traversal 

 class Solution(object):
        def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_copy = prices[:]
        prices_copy.sort(reverse=True)
        count=0
        for i in range(len(prices)):
            if prices[i] != prices_copy[i]:
                break
            else:
                count+=1
        if count == len(prices)-1:
            return 0

        buy=10000
        profit=0
      
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
                
        return profit        
  
        
            
        