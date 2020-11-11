import sys
import heapq

prices = []
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    prices.append(-1 * int(line))

n = -1 * prices[0]
prices = prices[1:]
heapq.heapify(prices)

group_size = 0
total_price = 0
while len(prices) > 0:
    nextMax = heapq.heappop(prices)
    group_size += 1
    if group_size % 3 != 0:
        total_price -= nextMax

print(total_price)
