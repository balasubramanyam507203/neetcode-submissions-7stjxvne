class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0

        for current in prices:
            min_price = min(min_price, current)
            max_price = max(max_price, current-min_price)
        return max_price
        