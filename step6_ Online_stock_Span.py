'''online stock span problem
explain the problem and solution in detail
the stock span problem is a financial problem that asks for the number of consecutive days leading up to the current day where the stock price was less than or equal to the current day's price.

For example, if the stock prices for the last 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock span for each day would be [1, 1, 1, 2, 1, 4, 6]. This means that on the first day (price 100), there is no previous day with a lower price, so the span is 1. On the second day (price 80), there is one previous day with a lower price (100), so the span is also 1. On the third day (price 60), there are two previous days with lower prices (100 and 80), so the span is 1. On the fourth day (price 70), there are three previous days with lower prices (100, 80, and 60), so the span is 2. On the fifth day (price 60), there are four previous days with lower prices (100, 80, 60, and 70), so the span is 1. On the sixth day (price 75), there are five previous days with lower prices (100, 80, 60, 70, and 60), so the span is 4. Finally, on the seventh day (price 85), there are six previous days with lower prices (100, 80, 60, 70, 60, and 75), so the span is 6.
example:
input: [100, 80, 60, 70, 60, 75
, 85]
output: [1, 1, 1, 2, 1, 4, 6]
'''
def stockSpan(prices):
    stack = []
    span = 0 * len(prices) # initialize span array with 0s
    for i in range(len(prices)):
        while stack and prices[i] >= prices[stack[-1]]: # check if current price is greater than or equal to price at index on top of stack
            stack.pop() # pop indices of days with lower prices
        span[i] = i + 1 if not stack else i - stack[-1] # calculate span based on current index and index of last higher price
        stack.append(i) # add current index to stack
    return span
