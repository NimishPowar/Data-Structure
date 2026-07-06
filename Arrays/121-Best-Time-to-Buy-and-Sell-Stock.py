class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        if len(arr) <=1:
            return 0
        max_profit = 0
        min_price = arr[0]
        for i in range(1,len(arr)):
            if arr[i]<min_price:
                min_price = arr[i]

            profit = arr[i] - min_price

            if profit > max_profit:
                max_profit = profit
        return max_profit