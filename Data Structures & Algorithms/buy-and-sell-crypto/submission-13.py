class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy=0
        c_b=prices[buy]
        profit=0
        for sell in range(1,len(prices)):
            if prices[sell]<c_b:
                c_b=prices[sell]
                
            profit=prices[sell]-c_b
            if profit>max_profit:
                max_profit=prices[sell]-c_b
        if profit<0:
            return 0
        else:
            return max_profit
        







        
     


        