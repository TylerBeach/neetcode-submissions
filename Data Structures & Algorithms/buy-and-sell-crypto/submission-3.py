class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [10,1,5,6,7,1]
        #                    B S 
        # profit = 0
        # find where B < S
        # if profit is pos check next day

        buy_day = 0
        sell_day = 1

        if len(prices) < 2:
            return 0

        record = 0
        while sell_day < len(prices):
            profit = prices[sell_day] - prices[buy_day]
            record = max(record, profit)

            if profit <= 0:
                buy_day += 1 
                sell_day = buy_day + 1
            else:
                sell_day += 1    

        return record













