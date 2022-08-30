'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

class Solution:

    def print_h(self):
        print('------------')
        print('lower heap')
        print(self.lowerhalf)
        print('upper heap')
        print(self.upperhalf)
        print('---------------')

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lowerhalf = []  # store the small half, top is the largest in the small part
        self.upperhalf = []  # store the large half, top is the smallest in the large part

    def addNum(self, num):
        print()
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # The case for the first element, just add to the minheap
        if len(self.lowerhalf) == 0:
            print('first el add - to min heap , this num %d' % num)
            heapq.heappush(self.lowerhalf, -num)
            return

        # Now choose where to add the new element
        # If it is less than or equal the top of min heap, it can be accomodated under it else go to max heap
        if num <= -self.lowerhalf[0]:
            print('adding to lower, num %d ' % num)
            heapq.heappush(self.lowerhalf, -num)  # Go to the max Heap
            # (-ve sign because to implement max heap using the default heapq in python, we need to negate the values)
        else:
            print('adding to upper, num %d' % num)
            heapq.heappush(self.upperhalf, num)  # Go to the min Heap

        # Adjusting the balance

        # If the lowerhalf heap has more elements
        if len(self.lowerhalf) - len(self.upperhalf) == 2:
            print('lower heap is 2 item longer, pop from lower, push to upper')
            heapq.heappush(self.upperhalf, - heapq.heappop(self.lowerhalf))

        # If the upperhalf heap has more elements
        elif len(self.upperhalf) - len(self.lowerhalf) == 2:
            print('upper heap is 2 item longer, pop from upper, push to lower')
            heapq.heappush(self.lowerhalf, - heapq.heappop(self.upperhalf))

        self.print_h()

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # If both heaps have same number of elements return the avg
        # If not, then the root of the one with more elements, is the answer

        if len(self.lowerhalf) == len(self.upperhalf):
            print('even median')
            res = (- self.lowerhalf[0] + self.upperhalf[0])/2.0
            # - sign because lowerhalf has negative value
        elif len(self.lowerhalf) > len(self.upperhalf):
            print('lower is longer - return lower')
            res = -float(self.lowerhalf[0])
        else:
            print('upper is longer - return upper')

            res = float(self.upperhalf[0])

        print('median %.2f' % res)
        return res

--------------------------------------------------------------------------------------------------------------
class MedianFinder:

    def __init__(self):
        
        self.lower = []
        self.upper = []
        

    def addNum(self, num: int) -> None:
        
        if len(self.lower) == 0:
            heapq.heappush(self.lower, -num)
            return
        if num <= -self.lower[0]:
            heapq.heappush(self.lower,-num)
        else:
            heapq.heappush(self.upper,num)
        
        if len(self.lower) - len(self.upper) == 2:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        
        elif len(self.upper) - len(self.lower) == 2:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
        

    def findMedian(self) -> float:
        
        if len(self.lower) == len(self.upper):
            res = (-self.lower[0] + self.upper[0])/2.0
        
        elif len(self.lower) > len(self.upper):
            res = -float(self.lower[0])
        else:
            res = float(self.upper[0])
            
        return res
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
