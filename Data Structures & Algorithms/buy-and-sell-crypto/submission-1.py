class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # [7,1,5,3,6,4]
        # buy low sell high -> left to right track min and compare to the current 
        lowest = prices[0]
        record = 0

        for price in prices:
            if price < lowest:
                lowest = price

            curr_profit = price - lowest
            record = max(record, curr_profit)

        return record