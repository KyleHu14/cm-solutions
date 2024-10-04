class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two Pointer Solution
        if len(prices) < 2:
            return 0

        buy_index = 0
        sell_index = 1
        max_profit = 0

        while buy_index < len(prices) and sell_index < len(prices):
            # 1. If buying price > selling price, check another buying price
            if prices[buy_index] > prices[sell_index]:
                buy_index += 1
            # 2. If buy & sell indexes are the same, increment the sell index
            elif buy_index == sell_index:
                sell_index += 1
            # 3. This means buying_price < selling_price
            else:
                max_profit = max(max_profit, prices[sell_index] - prices[buy_index])
                sell_index += 1
        
        return max_profit

        # Pure Array No Extra Techniques Solution
        min_buy = prices[0]
        max_profit = 0

        for sell_price in prices[1:]:
            max_profit = max(max_profit, sell_price - min_buy)

            min_buy = min(min_buy, sell_price)
        return max_profit
