class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to keep track of the minimum price and maximum profit.
        min1 = prices[0]  # Initialize 'min1' with the first price in the list.
        max1 = 0  # Initialize 'max1' with 0 as the initial maximum profit.

        # Loop through the list of stock prices.
        for i in prices:
            if min1 > i:
                # If the current price is smaller than the minimum price seen so far,
                # update the minimum price to the current price.
                min1 = i
            elif i - min1 > max1:
                # If selling at the current price results in a larger profit than the
                # maximum profit seen so far, update the maximum profit.
                max1 = i - min1

        # Return the maximum profit obtained by buying and selling the stock.
        return max1
