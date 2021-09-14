class Solution:
    def maxProfit(self, prices) -> int:
        if not prices or len(prices) == 0:
            return
        for i in range(1,len(prices)):
            if prices[i] > prices[i - 1]:
                break
            if i == len(prices) - 1:
                return 0

        min_price = prices[0]
        date = 0
        dif = 0
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            if price - min_price > dif:
                dif = price - min_price
                date = i
        return date+1

if __name__ == '__main__':
    sol=Solution()
    sol.maxProfit([1,2])