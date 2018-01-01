'''
Consider stock prices [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]. Write
a function that takes an input of stock prices and returns the maximum profit that
could be achieved by buying once and selling once.
'''

##The trick here is going forwards and then backwards
def double_transaction(prices):
    ##Do the exact same thing that we did for a single transaction
    max_profit, lowest_price = 0, float('inf')

    ##Keep track of the profits that can be made on that day, if there is a loss
    ##then treat it as 0 profit (no sell)
    first_transactions = [0] * len(prices)

    for i, price in enumerate(prices):
        this_profit = price - lowest_price
        max_profit = max(max_profit, this_profit)
        lowest_price = min(price, lowest_price)
        first_transactions[i] = this_profit if this_profit > 0 else 0

    # print(first_transactions)

    ##Now, for the trick. Go backwards. In this way, we are seeing what would
    ##happen if we backtrack the price from the last day back to the first.
    ##The profit that can be made on this day is whatever the highest price has
    ##been (not lowest, going backwards) - the current price but added in the
    ##profits that were made in the forward transactions. This way, we can see
    ##what profits could be made by looking at an additional sale
    max_price = float('-inf')
    second_transactions = [0] * len(prices)

    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price = max(max_price, price)
        this_profit = max_price - price + first_transactions[i -1]
        max_profit = max(max_profit, this_profit)
        second_transactions[i] = this_profit if this_profit > 0 else 0

    ##The maximum value here is the most profit that can be made
    # print(second_transactions)

    return max_profit

print(double_transaction([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
print(double_transaction([12,11,13,9,12,8,14,13,15]))

##Real stock data
NASDAQ = [6956, 6951, 6955, 6954, 6950, 6956, 6950, 6954, 6948, 6951, 6950, 6953, 6958, 6959, 6955, 6960, 6958, 6960, 6962, 6958, 6956, 6960]
print(double_transaction(NASDAQ))
