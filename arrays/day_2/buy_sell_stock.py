class BuySellStock:

    def __init__(self, prices):
        self.prices = prices

    def find_max_profit(self):
        max_profit = 0
        buy_price = self.prices[0]
        for i in range(1, len(self.prices)):
            if self.prices[i] < buy_price:
                buy_price = self.prices[i]
            else:
                profit = self.prices[i] - buy_price
                max_profit = max(profit, max_profit)
        return max_profit


if __name__ == '__main__':
    buy_sell_stock = BuySellStock([10, 1, 5, 6, 7, 1])
    print(buy_sell_stock.find_max_profit())
