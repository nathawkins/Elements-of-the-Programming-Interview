'''
Consider stock prices [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]. Write
a function that takes an input of stock prices and returns the maximum profit that
could be achieved by buying once and selling once.
'''

def single_transaction(prices):
    max_profit, lowest_price = 0, prices[0]

    worthy_transactions = []

    for price in prices:
        this_profit = price - lowest_price
        max_profit = max(max_profit, this_profit)
        if max_profit == this_profit:
            worthy_transactions.append([(lowest_price, price), this_profit])
        lowest_price = min(price, lowest_price)

    print("Buy: ${}. Sell: ${}. Profit: ${}.".format(worthy_transactions[-1][0][0], worthy_transactions[-1][0][1], worthy_transactions[-1][1]))

    return max_profit

print(single_transaction([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

##Real stock data
NASDAQ = [6956, 6951, 6955, 6954, 6950, 6956, 6950, 6954, 6948, 6951, 6950, 6953, 6958, 6959, 6955, 6960, 6958, 6960, 6962, 6958, 6956, 6960]
print(single_transaction(NASDAQ))
