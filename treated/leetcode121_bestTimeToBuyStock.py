"""
121. Best Time to Buy and Sell Stock
Easy
25.4K
795
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len(prices)
        l = 0  # Initialize left pointer
        r = 1  # Initialize right pointer
        max_profit = 0  # Initialize max_profit variable to store the maximum profit found
        while r < len(prices):  # Iterate until the right pointer reaches the end of the prices list
            if prices[l] < prices[r]:  # If the price at the left pointer is less than the price at the right pointer
                max_profit = max(max_profit, prices[r] - prices[l])  # Calculate the profit and update max_profit if necessary
            else:
                l = r  # If the price at the left pointer is greater or equal to the price at the right pointer, update the left pointer
            r += 1  # Move the right pointer to the next element
        return max_profit  # Return the maximum profit found
    
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
    prices[9]
    print(maxProfit(prices))