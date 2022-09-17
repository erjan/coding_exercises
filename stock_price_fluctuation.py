'''
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.
'''


class StockPrice:

    def __init__(self):
        self.latest_prices = {}
        self.time = 1
        self.min_prices = []
        self.max_prices = []
        heapify(self.min_prices)
        heapify(self.max_prices)

    def update(self, timestamp: int, price: int) -> None:
        self.latest_prices[timestamp] = price
        self.time = max(self.time, timestamp)
        heapq.heappush(self.min_prices, (price,timestamp))
        heapq.heappush(self.max_prices, (-price,timestamp))

    def current(self) -> int:
        return self.latest_prices[self.time]

    def maximum(self) -> int:
        top = self.max_prices[0]
        while self.latest_prices[top[1]] != -top[0]:
            heapq.heappop(self.max_prices)
            top = self.max_prices[0]
        return -top[0]

    def minimum(self) -> int:
        top = self.min_prices[0]
        while self.latest_prices[top[1]] != top[0]:
            heapq.heappop(self.min_prices)
            top = self.min_prices[0]
        return top[0]
------------------------------------------------------------------
from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
      
      self.current_stamp = -1
      self.records = {}
      self.prices = SortedList()
      
      
    def update(self, timestamp: int, price: int) -> None:
      
        if timestamp in self.records:
          self.prices.remove(self.records[timestamp])
          
        self.records[timestamp] = price
        self.prices.add(price)
        self.current_stamp = max(self.current_stamp, timestamp)

        
    def current(self) -> int:
        return self.records[self.current_stamp]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]

      
